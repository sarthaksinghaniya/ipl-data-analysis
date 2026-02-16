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
