import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
from typing import Dict, Optional


class IPLVisualizer:
    """Handles visualization of IPL analysis results."""
    
    def __init__(self, output_dir: str = "output"):
        self.output_dir = output_dir
        sns.set_style("whitegrid")
        os.makedirs(output_dir, exist_ok=True)
    
    def plot_max_margin_victories(self, max_run_win: pd.Series, max_wicket_win: pd.Series) -> None:
        """Plot maximum run and wicket margin victories."""
        # Maximum run margin
        plt.figure(figsize=(6, 4))
        plt.bar(max_run_win['winner'], max_run_win['win_by_runs'])
        plt.title("Maximum Run Margin Victory")
        plt.ylabel("Runs")
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, "max_run_margin.png"))
        plt.close()
        
        # Maximum wicket margin
        plt.figure(figsize=(6, 4))
        plt.bar(max_wicket_win['winner'], max_wicket_win['win_by_wickets'])
        plt.title("Maximum Wicket Margin Victory")
        plt.ylabel("Wickets")
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, "max_wicket_margin.png"))
        plt.close()
    
    def plot_city_matches(self, city_matches: pd.Series, top_n: int = 20) -> None:
        """Plot number of matches per city."""
        plt.figure(figsize=(12, 6))
        city_matches.head(top_n).plot(kind='bar')
        plt.title(f"Top {top_n} Cities by Number of Matches")
        plt.ylabel("Matches")
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, "matches_per_city.png"))
        plt.close()
    
    def plot_team_wins(self, team_wins: pd.Series) -> None:
        """Plot matches won by each team."""
        plt.figure(figsize=(12, 6))
        team_wins.plot(kind='bar')
        plt.title("Matches Won by Each Team")
        plt.ylabel("Wins")
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, "matches_won_by_team.png"))
        plt.close()
    
    def plot_toss_decision(self, toss_decision: pd.Series) -> None:
        """Plot toss decision distribution."""
        plt.figure(figsize=(6, 6))
        toss_decision.plot(kind='pie', autopct='%1.1f%%')
        plt.title("Toss Decision Distribution")
        plt.ylabel("")
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, "toss_decision_distribution.png"))
        plt.close()
    
    def plot_top_players(self, top_mom: pd.Series, top_six_hitters: pd.Series) -> None:
        """Plot top players by Man of Match awards and sixes."""
        # Man of Match awards
        plt.figure(figsize=(12, 6))
        top_mom.plot(kind='bar')
        plt.title("Top 10 Players - Man of the Match Awards")
        plt.ylabel("Awards")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, "top_10_mom_players.png"))
        plt.close()
        
        # Six hitters
        plt.figure(figsize=(12, 6))
        top_six_hitters.plot(kind='bar')
        plt.title("Top 10 Players with Most Sixes")
        plt.ylabel("Sixes")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, "top_10_six_hitters.png"))
        plt.close()
    
    def plot_dl_analysis(self, dl_per_season: pd.Series) -> None:
        """Plot Duckworth-Lewis applications per season."""
        plt.figure(figsize=(12, 6))
        dl_per_season.plot(kind='bar')
        plt.title("D/L Applied Per Season")
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, "dl_per_season.png"))
        plt.close()
    
    def plot_defending_chasing(self, best_defending: pd.Series, best_chasing: pd.Series,
                              venue_defend: pd.Series, venue_chase: pd.Series) -> None:
        """Plot defending and chasing statistics."""
        # Best defending teams
        plt.figure(figsize=(12, 6))
        best_defending.head(10).plot(kind='bar')
        plt.title("Top Defending Teams")
        plt.ylabel("Wins")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, "top_defending_teams.png"))
        plt.close()
        
        # Best chasing teams
        plt.figure(figsize=(12, 6))
        best_chasing.head(10).plot(kind='bar')
        plt.title("Top Chasing Teams")
        plt.ylabel("Wins")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, "top_chasing_teams.png"))
        plt.close()
        
        # Best venues for defending
        plt.figure(figsize=(12, 6))
        venue_defend.head(10).plot(kind='bar')
        plt.title("Best Venues for Defending")
        plt.ylabel("Matches")
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, "best_venues_defending.png"))
        plt.close()
        
        # Best venues for chasing
        plt.figure(figsize=(12, 6))
        venue_chase.head(10).plot(kind='bar')
        plt.title("Best Venues for Chasing")
        plt.ylabel("Matches")
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, "best_venues_chasing.png"))
        plt.close()
    
    def plot_rohit_sharma_career_analysis(self, rohit_analysis: Dict) -> None:
        """Create comprehensive visualizations for Rohit Sharma's career analysis."""
        
        # 1. Season-wise Performance
        self._plot_rohit_season_performance(rohit_analysis['season_performance'])
        
        # 2. Team-wise Performance
        self._plot_rohit_team_performance(rohit_analysis['team_performance'])
        
        # 3. Dismissal Analysis
        self._plot_rohit_dismissal_analysis(rohit_analysis['dismissal_analysis'])
        
        # 4. Phase-wise Performance
        self._plot_rohit_phase_performance(rohit_analysis['phase_performance'])
        
        # 5. Innings-wise Performance
        self._plot_rohit_innings_performance(rohit_analysis['innings_performance'])
        
        # 6. Consistency Analysis
        self._plot_rohit_consistency(rohit_analysis['consistency'])
        
        # 7. Top Venues Performance
        self._plot_rohit_venue_performance(rohit_analysis['venue_performance'])
        
        # 8. Career Milestones
        self._plot_rohit_milestones(rohit_analysis['milestones'])
    
    def _plot_rohit_season_performance(self, season_performance: Dict) -> None:
        """Plot Rohit's performance across seasons."""
        if not season_performance:
            return
            
        seasons = list(season_performance.keys())
        runs = [season_performance[season]['runs'] for season in seasons]
        strike_rates = [season_performance[season]['strike_rate'] for season in seasons]
        
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))
        
        # Runs per season
        ax1.bar(seasons, runs, color='skyblue')
        ax1.set_title("Rohit Sharma - Runs Per Season")
        ax1.set_ylabel("Runs")
        ax1.tick_params(axis='x', rotation=45)
        
        # Strike rate per season
        ax2.plot(seasons, strike_rates, marker='o', color='orange', linewidth=2)
        ax2.set_title("Rohit Sharma - Strike Rate Per Season")
        ax2.set_ylabel("Strike Rate")
        ax2.set_xlabel("Season")
        ax2.tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, "rohit_season_performance.png"))
        plt.close()
    
    def _plot_rohit_team_performance(self, team_performance: Dict) -> None:
        """Plot Rohit's performance for different teams."""
        if not team_performance:
            return
            
        teams = list(team_performance.keys())
        runs = [team_performance[team]['runs'] for team in teams]
        strike_rates = [team_performance[team]['strike_rate'] for team in teams]
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Runs per team
        ax1.bar(teams, runs, color='lightgreen')
        ax1.set_title("Rohit Sharma - Runs Per Team")
        ax1.set_ylabel("Runs")
        ax1.tick_params(axis='x', rotation=45)
        
        # Strike rate per team
        ax2.bar(teams, strike_rates, color='lightcoral')
        ax2.set_title("Rohit Sharma - Strike Rate Per Team")
        ax2.set_ylabel("Strike Rate")
        ax2.tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, "rohit_team_performance.png"))
        plt.close()
    
    def _plot_rohit_dismissal_analysis(self, dismissal_analysis: Dict) -> None:
        """Plot Rohit's dismissal patterns."""
        if not dismissal_analysis:
            return
            
        dismissals = list(dismissal_analysis.keys())
        counts = list(dismissal_analysis.values())
        
        plt.figure(figsize=(10, 6))
        plt.bar(dismissals, counts, color='mediumpurple')
        plt.title("Rohit Sharma - Dismissal Patterns")
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, "rohit_dismissal_patterns.png"))
        plt.close()
    
    def _plot_rohit_phase_performance(self, phase_performance: Dict) -> None:
        """Plot Rohit's performance in different game phases."""
        if not phase_performance:
            return
            
        phases = list(phase_performance.keys())
        strike_rates = [phase_performance[phase]['strike_rate'] for phase in phases]
        averages = [phase_performance[phase]['average'] for phase in phases]
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Strike rate by phase
        ax1.bar(phases, strike_rates, color='gold')
        ax1.set_title("Rohit Sharma - Strike Rate by Game Phase")
        ax1.set_ylabel("Strike Rate")
        
        # Average by phase
        ax2.bar(phases, averages, color='tomato')
        ax2.set_title("Rohit Sharma - Average by Game Phase")
        ax2.set_ylabel("Average")
        
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, "rohit_phase_performance.png"))
        plt.close()
    
    def _plot_rohit_innings_performance(self, innings_performance: Dict) -> None:
        """Plot Rohit's performance in different innings."""
        if not innings_performance:
            return
            
        innings = list(innings_performance.keys())
        runs = [innings_performance[inning]['runs'] for inning in innings]
        strike_rates = [innings_performance[inning]['strike_rate'] for inning in innings]
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Runs by innings
        ax1.bar(innings, runs, color='lightblue')
        ax1.set_title("Rohit Sharma - Runs by Innings")
        ax1.set_ylabel("Runs")
        
        # Strike rate by innings
        ax2.bar(innings, strike_rates, color='lightpink')
        ax2.set_title("Rohit Sharma - Strike Rate by Innings")
        ax2.set_ylabel("Strike Rate")
        
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, "rohit_innings_performance.png"))
        plt.close()
    
    def _plot_rohit_consistency(self, consistency: Dict) -> None:
        """Plot Rohit's consistency metrics."""
        if not consistency:
            return
            
        metrics = ['Mean Score', 'Median Score', 'Std Deviation']
        values = [consistency.get('mean_score', 0), 
                 consistency.get('median_score', 0), 
                 consistency.get('std_deviation', 0)]
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Consistency metrics
        ax1.bar(metrics, values, color=['skyblue', 'lightgreen', 'salmon'])
        ax1.set_title("Rohit Sharma - Consistency Metrics")
        ax1.set_ylabel("Value")
        
        # Score distribution
        score_categories = ['Ducks', '30+', '50+']
        score_counts = [consistency.get('ducks', 0), 
                       consistency.get('scores_above_30', 0) - consistency.get('scores_above_50', 0),
                       consistency.get('scores_above_50', 0)]
        
        ax2.bar(score_categories, score_counts, color=['red', 'orange', 'green'])
        ax2.set_title("Rohit Sharma - Score Distribution")
        ax2.set_ylabel("Count")
        
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, "rohit_consistency_analysis.png"))
        plt.close()
    
    def _plot_rohit_venue_performance(self, venue_performance: Dict) -> None:
        """Plot Rohit's performance at top venues."""
        if not venue_performance:
            return
            
        # Sort venues by runs and take top 10
        sorted_venues = sorted(venue_performance.items(), 
                            key=lambda x: x[1]['runs'], reverse=True)[:10]
        
        venues = [venue[0] for venue in sorted_venues]
        runs = [venue[1]['runs'] for venue in sorted_venues]
        
        plt.figure(figsize=(14, 8))
        plt.barh(venues, runs, color='teal')
        plt.title("Rohit Sharma - Top 10 Venues by Runs Scored")
        plt.xlabel("Runs")
        plt.ylabel("Venues")
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, "rohit_venue_performance.png"))
        plt.close()
    
    def _plot_rohit_milestones(self, milestones: Dict) -> None:
        """Plot Rohit's career milestones."""
        if not milestones:
            return
            
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Highest scores
        high_scores = milestones.get('highest_scores', [])[:10]
        match_numbers = list(range(1, len(high_scores) + 1))
        
        ax1.bar(match_numbers, high_scores, color='gold')
        ax1.set_title("Rohit Sharma - Top 10 Highest Scores")
        ax1.set_xlabel("Match Rank")
        ax1.set_ylabel("Score")
        
        # Centuries vs Half-centuries
        milestone_types = ['Half-Centuries', 'Centuries']
        milestone_counts = [milestones.get('half_centuries', 0), milestones.get('centuries', 0)]
        
        ax2.bar(milestone_types, milestone_counts, color=['orange', 'green'])
        ax2.set_title("Rohit Sharma - Career Milestones")
        ax2.set_ylabel("Count")
        
        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, "rohit_milestones.png"))
        plt.close()
