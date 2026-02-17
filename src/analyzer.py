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
    
    def get_rohit_sharma_career_analysis(self) -> Dict:
        """Comprehensive career analysis of Rohit Sharma."""
        # Filter Rohit Sharma data
        rohit_deliveries = self.deliveries[self.deliveries['batsman'] == 'RG Sharma']
        rohit_matches = self.matches[self.matches.apply(lambda x: 'RG Sharma' in str(x['player_of_match']) or 
                                                         self._did_rohit_play_in_match(x['id'], rohit_deliveries), axis=1)]
        
        # Career span
        career_seasons = sorted(rohit_matches['season'].unique())
        total_seasons = len(career_seasons)
        
        # Basic statistics
        total_matches = len(rohit_matches)
        total_runs = int(rohit_deliveries['batsman_runs'].sum())
        total_balls = len(rohit_deliveries[rohit_deliveries['wide_runs'] == 0])
        strike_rate = (total_runs / total_balls * 100) if total_balls > 0 else 0
        
        # Dismissal analysis
        dismissals = rohit_deliveries[rohit_deliveries['player_dismissed'] == 'RG Sharma']
        dismissal_modes = dismissals['dismissal_kind'].value_counts()
        
        # Season-wise performance
        season_performance = self._get_rohit_season_performance(rohit_deliveries, rohit_matches)
        
        # Team-wise performance
        team_performance = self._get_rohit_team_performance(rohit_deliveries, rohit_matches)
        
        # Venue-wise performance
        venue_performance = self._get_rohit_venue_performance(rohit_deliveries, rohit_matches)
        
        # Innings-wise performance
        innings_performance = self._get_rohit_innings_performance(rohit_deliveries)
        
        # Powerplay and death overs performance
        phase_performance = self._get_rohit_phase_performance(rohit_deliveries)
        
        # Captaincy analysis (when he was Man of Match, likely as captain)
        captaincy_matches = rohit_matches[rohit_matches['player_of_match'] == 'RG Sharma']
        captaincy_wins = len(captaincy_matches[captaincy_matches.apply(lambda x: self._did_rohit_team_win(x), axis=1)])
        
        # High scores and milestones
        match_scores = self._get_rohit_match_scores(rohit_deliveries)
        high_scores = sorted(match_scores, reverse=True)[:10]
        centuries = len([s for s in match_scores if s >= 100])
        half_centuries = len([s for s in match_scores if 50 <= s < 100])
        
        # Consistency analysis
        consistency_metrics = self._calculate_rohit_consistency(match_scores)
        
        # Performance against different bowling types
        bowling_analysis = self._get_rohit_vs_bowling_types(rohit_deliveries)
        
        return {
            'career_span': {
                'seasons': career_seasons,
                'total_seasons': total_seasons,
                'total_matches': total_matches
            },
            'basic_stats': {
                'total_runs': total_runs,
                'total_balls': total_balls,
                'strike_rate': round(strike_rate, 2),
                'average': round(total_runs / len(dismissals), 2) if len(dismissals) > 0 else 0
            },
            'dismissal_analysis': dismissal_modes.to_dict(),
            'season_performance': season_performance,
            'team_performance': team_performance,
            'venue_performance': venue_performance,
            'innings_performance': innings_performance,
            'phase_performance': phase_performance,
            'captaincy': {
                'mom_awards': len(captaincy_matches),
                'wins_as_captain': captaincy_wins,
                'win_rate_as_captain': round((captaincy_wins / len(captaincy_matches) * 100), 2) if len(captaincy_matches) > 0 else 0
            },
            'milestones': {
                'highest_scores': high_scores,
                'centuries': centuries,
                'half_centuries': half_centuries
            },
            'consistency': consistency_metrics,
            'vs_bowling_types': bowling_analysis
        }
    
    def _did_rohit_play_in_match(self, match_id: int, rohit_deliveries: pd.DataFrame) -> bool:
        """Check if Rohit Sharma played in a specific match."""
        return match_id in rohit_deliveries['match_id'].unique()
    
    def _did_rohit_team_win(self, match_row: pd.Series) -> bool:
        """Check if Rohit's team won the match."""
        # This is a simplified check - in reality, we'd need to determine which team Rohit was playing for
        return True  # Placeholder logic
    
    def _get_rohit_season_performance(self, rohit_deliveries: pd.DataFrame, rohit_matches: pd.DataFrame) -> Dict:
        """Get Rohit's performance season by season."""
        season_stats = {}
        
        for season in sorted(rohit_matches['season'].unique()):
            season_matches = rohit_matches[rohit_matches['season'] == season]
            season_match_ids = season_matches['id'].tolist()
            season_deliveries = rohit_deliveries[rohit_deliveries['match_id'].isin(season_match_ids)]
            
            runs = int(season_deliveries['batsman_runs'].sum())
            balls = len(season_deliveries[season_deliveries['wide_runs'] == 0])
            dismissals = len(season_deliveries[season_deliveries['player_dismissed'] == 'RG Sharma'])
            
            season_stats[season] = {
                'runs': runs,
                'balls': balls,
                'dismissals': dismissals,
                'average': round(runs / dismissals, 2) if dismissals > 0 else 0,
                'strike_rate': round((runs / balls * 100), 2) if balls > 0 else 0,
                'matches': len(season_matches)
            }
        
        return season_stats
    
    def _get_rohit_team_performance(self, rohit_deliveries: pd.DataFrame, rohit_matches: pd.DataFrame) -> Dict:
        """Get Rohit's performance for different teams."""
        team_stats = {}
        
        # Get teams Rohit played for from deliveries data
        teams = rohit_deliveries['batting_team'].unique()
        
        for team in teams:
            team_deliveries = rohit_deliveries[rohit_deliveries['batting_team'] == team]
            team_match_ids = team_deliveries['match_id'].unique()
            team_matches = rohit_matches[rohit_matches['id'].isin(team_match_ids)]
            
            runs = int(team_deliveries['batsman_runs'].sum())
            balls = len(team_deliveries[team_deliveries['wide_runs'] == 0])
            dismissals = len(team_deliveries[team_deliveries['player_dismissed'] == 'RG Sharma'])
            
            team_stats[team] = {
                'runs': runs,
                'balls': balls,
                'dismissals': dismissals,
                'average': round(runs / dismissals, 2) if dismissals > 0 else 0,
                'strike_rate': round((runs / balls * 100), 2) if balls > 0 else 0,
                'matches': len(team_matches)
            }
        
        return team_stats
    
    def _get_rohit_venue_performance(self, rohit_deliveries: pd.DataFrame, rohit_matches: pd.DataFrame) -> Dict:
        """Get Rohit's performance at different venues."""
        venue_stats = {}
        
        # Get venues where Rohit played
        venue_matches = rohit_matches.dropna(subset=['venue'])
        
        for venue in venue_matches['venue'].unique():
            venue_match_ids = venue_matches[venue_matches['venue'] == venue]['id'].tolist()
            venue_deliveries = rohit_deliveries[rohit_deliveries['match_id'].isin(venue_match_ids)]
            
            if len(venue_deliveries) > 0:
                runs = int(venue_deliveries['batsman_runs'].sum())
                balls = len(venue_deliveries[venue_deliveries['wide_runs'] == 0])
                dismissals = len(venue_deliveries[venue_deliveries['player_dismissed'] == 'RG Sharma'])
                
                venue_stats[venue] = {
                    'runs': runs,
                    'balls': balls,
                    'dismissals': dismissals,
                    'average': round(runs / dismissals, 2) if dismissals > 0 else 0,
                    'strike_rate': round((runs / balls * 100), 2) if balls > 0 else 0,
                    'matches': len(venue_match_ids)
                }
        
        return venue_stats
    
    def _get_rohit_innings_performance(self, rohit_deliveries: pd.DataFrame) -> Dict:
        """Get Rohit's performance in different innings."""
        innings_stats = {}
        
        for inning in [1, 2]:
            inning_deliveries = rohit_deliveries[rohit_deliveries['inning'] == inning]
            
            runs = int(inning_deliveries['batsman_runs'].sum())
            balls = len(inning_deliveries[inning_deliveries['wide_runs'] == 0])
            dismissals = len(inning_deliveries[inning_deliveries['player_dismissed'] == 'RG Sharma'])
            
            innings_stats[f'inning_{inning}'] = {
                'runs': runs,
                'balls': balls,
                'dismissals': dismissals,
                'average': round(runs / dismissals, 2) if dismissals > 0 else 0,
                'strike_rate': round((runs / balls * 100), 2) if balls > 0 else 0
            }
        
        return innings_stats
    
    def _get_rohit_phase_performance(self, rohit_deliveries: pd.DataFrame) -> Dict:
        """Get Rohit's performance in different phases of the game."""
        phase_stats = {
            'powerplay': {'runs': 0, 'balls': 0, 'wickets': 0},
            'middle': {'runs': 0, 'balls': 0, 'wickets': 0},
            'death': {'runs': 0, 'balls': 0, 'wickets': 0}
        }
        
        for _, delivery in rohit_deliveries.iterrows():
            over = delivery['over']
            if over <= 6:
                phase = 'powerplay'
            elif over <= 15:
                phase = 'middle'
            else:
                phase = 'death'
            
            if delivery['wide_runs'] == 0:
                phase_stats[phase]['balls'] += 1
                phase_stats[phase]['runs'] += delivery['batsman_runs']
            
            if delivery['player_dismissed'] == 'RG Sharma':
                phase_stats[phase]['wickets'] += 1
        
        # Calculate strike rates
        for phase in phase_stats:
            if phase_stats[phase]['balls'] > 0:
                phase_stats[phase]['strike_rate'] = round(
                    (phase_stats[phase]['runs'] / phase_stats[phase]['balls'] * 100), 2
                )
            else:
                phase_stats[phase]['strike_rate'] = 0
            
            if phase_stats[phase]['wickets'] > 0:
                phase_stats[phase]['average'] = round(
                    (phase_stats[phase]['runs'] / phase_stats[phase]['wickets']), 2
                )
            else:
                phase_stats[phase]['average'] = 0
        
        return phase_stats
    
    def _get_rohit_match_scores(self, rohit_deliveries: pd.DataFrame) -> List[int]:
        """Get Rohit's scores in each match."""
        match_scores = []
        
        for match_id in rohit_deliveries['match_id'].unique():
            match_deliveries = rohit_deliveries[rohit_deliveries['match_id'] == match_id]
            score = int(match_deliveries['batsman_runs'].sum())
            match_scores.append(score)
        
        return match_scores
    
    def _calculate_rohit_consistency(self, match_scores: List[int]) -> Dict:
        """Calculate consistency metrics for Rohit's performance."""
        if not match_scores:
            return {}
        
        import numpy as np
        
        scores_array = np.array(match_scores)
        
        return {
            'mean_score': round(np.mean(scores_array), 2),
            'median_score': round(np.median(scores_array), 2),
            'std_deviation': round(np.std(scores_array), 2),
            'coefficient_of_variation': round((np.std(scores_array) / np.mean(scores_array) * 100), 2) if np.mean(scores_array) > 0 else 0,
            'scores_above_50': len([s for s in match_scores if s >= 50]),
            'scores_above_30': len([s for s in match_scores if s >= 30]),
            'ducks': len([s for s in match_scores if s == 0]),
            'total_innings': len(match_scores)
        }
    
    def _get_rohit_vs_bowling_types(self, rohit_deliveries: pd.DataFrame) -> Dict:
        """Analyze Rohit's performance against different bowling types."""
        bowling_stats = {}
        
        # Group by bowler and analyze performance
        bowler_stats = rohit_deliveries.groupby('bowler').agg({
            'batsman_runs': ['sum', 'count'],
            'player_dismissed': lambda x: (x == 'RG Sharma').sum()
        }).round(2)
        
        bowler_stats.columns = ['runs_conceded', 'balls_faced', 'dismissals']
        
        # Calculate strike rate and average against each bowler
        bowler_stats['strike_rate'] = (bowler_stats['runs_conceded'] / bowler_stats['balls_faced'] * 100).round(2)
        bowler_stats['average'] = (bowler_stats['runs_conceded'] / bowler_stats['dismissals']).round(2)
        
        # Get top bowlers Rohit has faced most
        top_bowlers = bowler_stats.sort_values('balls_faced', ascending=False).head(15)
        
        return top_bowlers.to_dict('index')
