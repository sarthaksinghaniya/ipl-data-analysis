import pandas as pd
from typing import Dict, List, Tuple


class IPLAnalyzer:
    """Performs various analyses on IPL data."""
    
    def __init__(self, matches: pd.DataFrame, deliveries: pd.DataFrame):
        self.matches = matches
        self.deliveries = deliveries
    
    def get_max_margin_victories(self) -> Dict[str, pd.Series]:
        """Get maximum run and wicket margin victories."""
        max_run_win = self.matches.loc[self.matches['win_by_runs'].idxmax()]
        max_wicket_win = self.matches.loc[self.matches['win_by_wickets'].idxmax()]
        
        return {
            'max_run_win': max_run_win,
            'max_wicket_win': max_wicket_win
        }
    
    def get_city_stats(self) -> pd.Series:
        """Get number of matches per city."""
        return self.matches['city'].value_counts()
    
    def get_team_wins(self) -> pd.Series:
        """Get matches won by each team."""
        return self.matches['winner'].value_counts()
    
    def get_toss_analysis(self) -> Dict[str, float]:
        """Analyze toss decisions and their impact."""
        toss_match_win = self.matches[self.matches['toss_winner'] == self.matches['winner']]
        percentage = (len(toss_match_win) / len(self.matches)) * 100
        
        toss_decision = self.matches['toss_decision'].value_counts()
        
        return {
            'toss_winner_match_winner_percentage': percentage,
            'toss_decision_distribution': toss_decision
        }
    
    def get_top_players(self) -> Dict[str, pd.Series]:
        """Get top players by various metrics."""
        top_mom = self.matches['player_of_match'].value_counts().head(10)
        
        sixes = self.deliveries[self.deliveries['batsman_runs'] == 6]
        top_six_hitters = sixes['batsman'].value_counts().head(10)
        
        return {
            'top_man_of_match': top_mom,
            'top_six_hitters': top_six_hitters
        }
    
    def get_dl_analysis(self) -> Dict[str, pd.Series]:
        """Analyze Duckworth-Lewis applications."""
        dl_applied = self.matches['dl_applied'].value_counts()
        dl_season = self.matches.groupby('season')['dl_applied'].sum()
        
        return {
            'dl_applied_overall': dl_applied,
            'dl_per_season': dl_season
        }
    
    def get_defending_chasing_stats(self) -> Dict[str, pd.Series]:
        """Get defending and chasing statistics."""
        defending = self.matches[self.matches['win_by_runs'] > 0]
        chasing = self.matches[self.matches['win_by_wickets'] > 0]
        
        best_defending = defending['winner'].value_counts()
        best_chasing = chasing['winner'].value_counts()
        
        venue_defend = defending['venue'].value_counts()
        venue_chase = chasing['venue'].value_counts()
        
        return {
            'best_defending_teams': best_defending,
            'best_chasing_teams': best_chasing,
            'best_venues_defending': venue_defend,
            'best_venues_chasing': venue_chase
        }
    
    def get_business_insights(self) -> List[str]:
        """Generate business insights from the analysis."""
        return [
            "Cities with higher match frequency indicate strong engagement potential.",
            "Toss advantage exists but is not overwhelmingly decisive.",
            "Certain teams dominate defending and chasing conditions.",
            "Venue characteristics significantly impact match outcomes.",
            "High six-hitting players contribute strongly to audience engagement."
        ]
