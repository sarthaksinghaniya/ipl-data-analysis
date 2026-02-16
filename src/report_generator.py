import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from datetime import datetime
from typing import Dict, List, Any
import pandas as pd


class ReportGenerator:
    """Generates PDF reports for IPL analysis results."""
    
    def __init__(self, output_dir: str = "output"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def generate_comprehensive_report(self, 
                                    analysis_results: Dict[str, Any],
                                    visualizations: List[str] = None) -> str:
        """Generate a comprehensive PDF report with analysis results and visualizations."""
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        pdf_path = os.path.join(self.output_dir, f"ipl_analysis_report_{timestamp}.pdf")
        
        with PdfPages(pdf_path) as pdf:
            # Title page
            self._add_title_page(pdf)
            
            # Executive summary
            self._add_executive_summary(pdf, analysis_results)
            
            # Data overview
            self._add_data_overview(pdf, analysis_results)
            
            # Match analysis
            self._add_match_analysis(pdf, analysis_results)
            
            # Team performance
            self._add_team_performance(pdf, analysis_results)
            
            # Player analysis
            self._add_player_analysis(pdf, analysis_results)
            
            # Venue analysis
            self._add_venue_analysis(pdf, analysis_results)
            
            # Business insights
            self._add_business_insights(pdf, analysis_results)
            
            # Append visualizations if provided
            if visualizations:
                self._add_visualizations(pdf, visualizations)
        
        return pdf_path
    
    def _add_title_page(self, pdf: PdfPages):
        """Add title page to the PDF."""
        fig, ax = plt.subplots(figsize=(8.5, 11))
        ax.text(0.5, 0.8, 'IPL Data Analysis Report', 
                fontsize=24, fontweight='bold', ha='center')
        ax.text(0.5, 0.7, 'Comprehensive Analysis of Indian Premier League Data', 
                fontsize=14, ha='center')
        ax.text(0.5, 0.6, f'Generated on: {datetime.now().strftime("%B %d, %Y")}', 
                fontsize=12, ha='center')
        ax.text(0.5, 0.5, 'Confidential', 
                fontsize=10, style='italic', ha='center')
        ax.axis('off')
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
    
    def _add_executive_summary(self, pdf: PdfPages, results: Dict[str, Any]):
        """Add executive summary section."""
        fig, ax = plt.subplots(figsize=(8.5, 11))
        ax.text(0.05, 0.95, 'Executive Summary', fontsize=18, fontweight='bold')
        
        summary_text = f"""
This report presents a comprehensive analysis of IPL cricket data, covering {results.get('total_matches', 'N/A')} matches 
and {results.get('total_deliveries', 'N/A')} deliveries.

Key Findings:
• Total teams analyzed: {results.get('total_teams', 'N/A')}
• Cities hosting matches: {results.get('total_cities', 'N/A')}
• Seasons covered: {results.get('seasons_covered', 'N/A')}
• Toss winner advantage: {results.get('toss_advantage_pct', 'N/A')}%
• Average win margin by runs: {results.get('avg_win_margin_runs', 'N/A')}
• Average win margin by wickets: {results.get('avg_win_margin_wickets', 'N/A')}

The analysis reveals important patterns in team performance, venue characteristics, and player contributions 
that can inform strategic decisions for stakeholders.
        """
        
        ax.text(0.05, 0.85, summary_text, fontsize=10, verticalalignment='top')
        ax.axis('off')
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
    
    def _add_data_overview(self, pdf: PdfPages, results: Dict[str, Any]):
        """Add data overview section."""
        fig, ax = plt.subplots(figsize=(8.5, 11))
        ax.text(0.05, 0.95, 'Data Overview', fontsize=18, fontweight='bold')
        
        overview_text = f"""
Dataset Information:
• Matches dataset shape: {results.get('matches_shape', 'N/A')}
• Deliveries dataset shape: {results.get('deliveries_shape', 'N/A')}
• Data completeness: {results.get('data_completeness', 'N/A')}%

Data Quality Assessment:
• Missing values in matches: {results.get('matches_nulls', 'N/A')}
• Missing values in deliveries: {results.get('deliveries_nulls', 'N/A')}
• Data range: {results.get('date_range', 'N/A')}

The datasets provide comprehensive coverage of IPL matches including match-level information 
and detailed ball-by-ball data for in-depth analysis.
        """
        
        ax.text(0.05, 0.85, overview_text, fontsize=10, verticalalignment='top')
        ax.axis('off')
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
    
    def _add_match_analysis(self, pdf: PdfPages, results: Dict[str, Any]):
        """Add match analysis section."""
        fig, ax = plt.subplots(figsize=(8.5, 11))
        ax.text(0.05, 0.95, 'Match Analysis', fontsize=18, fontweight='bold')
        
        match_text = f"""
Victory Margins:
• Highest run margin victory: {results.get('max_run_margin_team', 'N/A')} by {results.get('max_run_margin', 'N/A')} runs
• Highest wicket margin victory: {results.get('max_wicket_margin_team', 'N/A')} by {results.get('max_wicket_margin', 'N/A')} wickets

Toss Analysis:
• Matches where toss winner won: {results.get('toss_winner_wins', 'N/A')} ({results.get('toss_advantage_pct', 'N/A')}%)
• Preferred toss decision: {results.get('preferred_toss_decision', 'N/A')}
• Field vs Bat choice distribution: {results.get('toss_decision_dist', 'N/A')}

Weather Impact:
• D/L method applied: {results.get('dl_applied_count', 'N/A')} times
• Seasons with most D/L applications: {results.get('dl_seasons', 'N/A')}
        """
        
        ax.text(0.05, 0.85, match_text, fontsize=10, verticalalignment='top')
        ax.axis('off')
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
    
    def _add_team_performance(self, pdf: PdfPages, results: Dict[str, Any]):
        """Add team performance section."""
        fig, ax = plt.subplots(figsize=(8.5, 11))
        ax.text(0.05, 0.95, 'Team Performance Analysis', fontsize=18, fontweight='bold')
        
        team_text = f"""
Top Performing Teams:
• Most wins: {results.get('top_winning_team', 'N/A')} ({results.get('top_team_wins', 'N/A')} wins)
• Best defending teams: {results.get('top_defending_teams', 'N/A')}
• Best chasing teams: {results.get('top_chasing_teams', 'N/A')}

Win Distribution:
• Average wins per team: {results.get('avg_wins_per_team', 'N/A')}
• Win distribution variance: {results.get('win_variance', 'N/A')}
• Most consistent performers: {results.get('consistent_teams', 'N/A')}

Venue Performance:
• Most active venues: {results.get('top_venues', 'N/A')}
• Best venues for defending: {results.get('best_defend_venues', 'N/A')}
• Best venues for chasing: {results.get('best_chase_venues', 'N/A')}
        """
        
        ax.text(0.05, 0.85, team_text, fontsize=10, verticalalignment='top')
        ax.axis('off')
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
    
    def _add_player_analysis(self, pdf: PdfPages, results: Dict[str, Any]):
        """Add player analysis section."""
        fig, ax = plt.subplots(figsize=(8.5, 11))
        ax.text(0.05, 0.95, 'Player Performance Analysis', fontsize=18, fontweight='bold')
        
        player_text = f"""
Top Players:
• Most Man of Match awards: {results.get('top_mom_player', 'N/A')} ({results.get('top_mom_count', 'N/A')} awards)
• Top six hitters: {results.get('top_six_hitter', 'N/A')} ({results.get('top_six_count', 'N/A')} sixes)
• Most consistent performers: {results.get('consistent_players', 'N/A')}

Player Impact:
• Average MoM per match: {results.get('avg_mom_per_match', 'N/A')}
• Six frequency: {results.get('six_frequency', 'N/A')} per match
• Player contribution to wins: {results.get('player_impact', 'N/A')}%

Emerging Talent:
• Rising performers: {results.get('emerging_players', 'N/A')}
• Breakout seasons: {results.get('breakout_seasons', 'N/A')}
        """
        
        ax.text(0.05, 0.85, player_text, fontsize=10, verticalalignment='top')
        ax.axis('off')
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
    
    def _add_venue_analysis(self, pdf: PdfPages, results: Dict[str, Any]):
        """Add venue analysis section."""
        fig, ax = plt.subplots(figsize=(8.5, 11))
        ax.text(0.05, 0.95, 'Venue Analysis', fontsize=18, fontweight='bold')
        
        venue_text = f"""
Venue Statistics:
• Total venues: {results.get('total_venues', 'N/A')}
• Most active venue: {results.get('most_active_venue', 'N/A')} ({results.get('most_active_matches', 'N/A')} matches)
• Cities with IPL presence: {results.get('total_cities', 'N/A')}

Venue Characteristics:
• High-scoring venues: {results.get('high_scoring_venues', 'N/A')}
• Bowler-friendly venues: {results.get('bowler_friendly_venues', 'N/A')}
• Venue win patterns: {results.get('venue_patterns', 'N/A')}

Geographic Distribution:
• Top cricket regions: {results.get('top_regions', 'N/A')}
• Emerging cricket hubs: {results.get('emerging_hubs', 'N/A')}
• Venue utilization rate: {results.get('venue_utilization', 'N/A')}%
        """
        
        ax.text(0.05, 0.85, venue_text, fontsize=10, verticalalignment='top')
        ax.axis('off')
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
    
    def _add_business_insights(self, pdf: PdfPages, results: Dict[str, Any]):
        """Add business insights section."""
        fig, ax = plt.subplots(figsize=(8.5, 11))
        ax.text(0.05, 0.95, 'Business Insights & Recommendations', fontsize=18, fontweight='bold')
        
        insights = results.get('business_insights', [
            "Cities with higher match frequency indicate strong engagement potential.",
            "Toss advantage exists but is not overwhelmingly decisive.",
            "Certain teams dominate defending and chasing conditions.",
            "Venue characteristics significantly impact match outcomes.",
            "High six-hitting players contribute strongly to audience engagement."
        ])
        
        insights_text = "Key Business Insights:\n\n"
        for i, insight in enumerate(insights, 1):
            insights_text += f"{i}. {insight}\n"
        
        insights_text += f"""

Strategic Recommendations:
• Focus marketing efforts on high-engagement cities: {results.get('target_cities', 'N/A')}
• Leverage popular players for brand building: {results.get('key_players', 'N/A')}
• Optimize scheduling based on venue characteristics: {results.get('schedule_optimization', 'N/A')}
• Develop content around team rivalries: {results.get('key_rivalries', 'N/A')}

Financial Implications:
• Revenue optimization opportunities: {results.get('revenue_opportunities', 'N/A')}
• Sponsorship value drivers: {results.get('sponsorship_drivers', 'N/A')}
• Fan engagement strategies: {results.get('engagement_strategies', 'N/A')}
        """
        
        ax.text(0.05, 0.85, insights_text, fontsize=10, verticalalignment='top')
        ax.axis('off')
        pdf.savefig(fig, bbox_inches='tight')
        plt.close()
    
    def _add_visualizations(self, pdf: PdfPages, visualization_paths: List[str]):
        """Add visualizations to the PDF."""
        for viz_path in visualization_paths:
            if os.path.exists(viz_path):
                try:
                    img = plt.imread(viz_path)
                    fig, ax = plt.subplots(figsize=(8.5, 11))
                    ax.imshow(img)
                    ax.axis('off')
                    pdf.savefig(fig, bbox_inches='tight')
                    plt.close()
                except Exception as e:
                    print(f"Could not add visualization {viz_path}: {e}")
    
    def generate_text_report(self, analysis_results: Dict[str, Any]) -> str:
        """Generate a text-only report."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        txt_path = os.path.join(self.output_dir, f"ipl_analysis_text_{timestamp}.txt")
        
        with open(txt_path, 'w', encoding='utf-8') as f:
            f.write("IPL DATA ANALYSIS REPORT\n")
            f.write("=" * 50 + "\n\n")
            f.write(f"Generated on: {datetime.now().strftime('%B %d, %Y %H:%M:%S')}\n\n")
            
            # Write all analysis results
            for key, value in analysis_results.items():
                f.write(f"{key.upper()}\n")
                f.write("-" * 30 + "\n")
                f.write(f"{value}\n\n")
        
        return txt_path
