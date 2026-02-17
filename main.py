"""
IPL Data Analysis - Main Entry Point

This script performs comprehensive analysis of IPL cricket data including:
- Match statistics and team performance
- Player performance metrics
- Venue analysis
- Toss and weather impact analysis
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.data_loader import DataLoader
from src.analyzer import IPLAnalyzer
from src.visualizer import IPLVisualizer
from src.report_generator import ReportGenerator
from src.rohit_sharma_report_generator import RohitSharmaReportGenerator


def main():
    """Main function to run the IPL analysis pipeline."""
    
    print("=" * 60)
    print("IPL DATA ANALYSIS PIPELINE")
    print("=" * 60)
    
    # Initialize components
    loader = DataLoader()
    report_generator = ReportGenerator()
    rohit_report_generator = RohitSharmaReportGenerator()
    
    # Load data
    print("\n1. Loading data...")
    matches, deliveries = loader.load_data()
    
    # Display data information
    sample_matches, sample_deliveries = loader.get_sample_data()
    print("\nSample matches data:")
    print(sample_matches)
    print("\nSample deliveries data:")
    print(sample_deliveries)
    
    data_info = loader.get_data_info()
    print(f"\nMatches shape: {data_info['matches_shape']}")
    print(f"Deliveries shape: {data_info['deliveries_shape']}")
    
    # Initialize analyzer
    analyzer = IPLAnalyzer(matches, deliveries)
    
    # Perform analyses
    print("\n2. Performing analyses...")
    
    # Maximum margin victories
    max_victories = analyzer.get_max_margin_victories()
    print("\nMaximum run margin victory:")
    print(max_victories['max_run_win'][['winner', 'win_by_runs']])
    print("\nMaximum wicket margin victory:")
    print(max_victories['max_wicket_win'][['winner', 'win_by_wickets']])
    
    # City statistics
    city_stats = analyzer.get_city_stats()
    print(f"\nTop 5 cities by matches:")
    print(city_stats.head())
    
    # Team wins
    team_wins = analyzer.get_team_wins()
    print(f"\nTop 5 teams by wins:")
    print(team_wins.head())
    
    # Toss analysis
    toss_analysis = analyzer.get_toss_analysis()
    print(f"\nToss winner won match percentage: {toss_analysis['toss_winner_match_winner_percentage']:.2f}%")
    print("\nToss decision distribution:")
    print(toss_analysis['toss_decision_distribution'])
    
    # Top players
    top_players = analyzer.get_top_players()
    print(f"\nTop 5 Man of Match award winners:")
    print(top_players['top_man_of_match'].head())
    print(f"\nTop 5 six hitters:")
    print(top_players['top_six_hitters'].head())
    
    # DL analysis
    dl_analysis = analyzer.get_dl_analysis()
    print(f"\nDL applied overall:")
    print(dl_analysis['dl_applied_overall'])
    print(f"\nDL applied per season:")
    print(dl_analysis['dl_per_season'])
    
    # Defending and chasing stats
    defend_chase_stats = analyzer.get_defending_chasing_stats()
    print(f"\nTop 5 defending teams:")
    print(defend_chase_stats['best_defending_teams'].head())
    print(f"\nTop 5 chasing teams:")
    print(defend_chase_stats['best_chasing_teams'].head())
    
    # Rohit Sharma Career Analysis
    print("\n3.1. Performing Rohit Sharma Career Analysis...")
    rohit_analysis = analyzer.get_rohit_sharma_career_analysis()
    
    print(f"\nRohit Sharma Career Summary:")
    print(f"Career Span: {rohit_analysis['career_span']['seasons'][0]} - {rohit_analysis['career_span']['seasons'][-1]}")
    print(f"Total Seasons: {rohit_analysis['career_span']['total_seasons']}")
    print(f"Total Matches: {rohit_analysis['career_span']['total_matches']}")
    print(f"Total Runs: {rohit_analysis['basic_stats']['total_runs']}")
    print(f"Strike Rate: {rohit_analysis['basic_stats']['strike_rate']}")
    print(f"Average: {rohit_analysis['basic_stats']['average']}")
    print(f"Centuries: {rohit_analysis['milestones']['centuries']}")
    print(f"Half-centuries: {rohit_analysis['milestones']['half_centuries']}")
    print(f"Man of Match Awards: {rohit_analysis['captaincy']['mom_awards']}")
    
    print(f"\nSeason-wise Performance (Last 5 seasons):")
    recent_seasons = list(rohit_analysis['season_performance'].keys())[-5:]
    for season in recent_seasons:
        stats = rohit_analysis['season_performance'][season]
        print(f"{season}: {stats['runs']} runs @ {stats['strike_rate']} SR, {stats['matches']} matches")
    
    # Initialize visualizer
    print("\n3. Generating visualizations...")
    visualizer = IPLVisualizer()
    
    # Create all visualizations
    visualizer.plot_max_margin_victories(
        max_victories['max_run_win'], 
        max_victories['max_wicket_win']
    )
    visualizer.plot_city_matches(city_stats)
    visualizer.plot_team_wins(team_wins)
    visualizer.plot_toss_decision(toss_analysis['toss_decision_distribution'])
    visualizer.plot_top_players(
        top_players['top_man_of_match'], 
        top_players['top_six_hitters']
    )
    visualizer.plot_dl_analysis(dl_analysis['dl_per_season'])
    visualizer.plot_defending_chasing(
        defend_chase_stats['best_defending_teams'],
        defend_chase_stats['best_chasing_teams'],
        defend_chase_stats['best_venues_defending'],
        defend_chase_stats['best_venues_chasing']
    )
    
    # Generate Rohit Sharma visualizations
    print("\n3.1. Generating Rohit Sharma visualizations...")
    visualizer.plot_rohit_sharma_career_analysis(rohit_analysis)
    
    # Display business insights
    print("\n4. Business Insights:")
    insights = analyzer.get_business_insights()
    for i, insight in enumerate(insights, 1):
        print(f"{i}. {insight}")
    
    # Generate comprehensive analysis results for report
    print("\n5. Preparing analysis results for report...")
    analysis_results = {
        'total_matches': len(matches),
        'total_deliveries': len(deliveries),
        'total_teams': len(matches['team1'].unique()),
        'total_cities': len(matches['city'].unique()),
        'seasons_covered': len(matches['season'].unique()),
        'matches_shape': matches.shape,
        'deliveries_shape': deliveries.shape,
        'toss_advantage_pct': f"{toss_analysis['toss_winner_match_winner_percentage']:.2f}",
        'max_run_margin_team': max_victories['max_run_win']['winner'],
        'max_run_margin': max_victories['max_run_win']['win_by_runs'],
        'max_wicket_margin_team': max_victories['max_wicket_win']['winner'],
        'max_wicket_margin': max_victories['max_wicket_win']['win_by_wickets'],
        'top_winning_team': team_wins.index[0],
        'top_team_wins': team_wins.iloc[0],
        'top_mom_player': top_players['top_man_of_match'].index[0],
        'top_mom_count': top_players['top_man_of_match'].iloc[0],
        'top_six_hitter': top_players['top_six_hitters'].index[0],
        'top_six_count': top_players['top_six_hitters'].iloc[0],
        'business_insights': insights,
        'preferred_toss_decision': toss_analysis['toss_decision_distribution'].index[0],
        'dl_applied_count': dl_analysis['dl_applied_overall'].get(1, 0),
        'rohit_sharma_analysis': rohit_analysis
    }
    
    # Generate PDF report
    print("\n6. Generating PDF report...")
    visualization_paths = [
        os.path.join("output", "max_run_margin.png"),
        os.path.join("output", "max_wicket_margin.png"),
        os.path.join("output", "matches_per_city.png"),
        os.path.join("output", "matches_won_by_team.png"),
        os.path.join("output", "toss_decision_distribution.png"),
        os.path.join("output", "top_10_mom_players.png"),
        os.path.join("output", "top_10_six_hitters.png"),
        os.path.join("output", "dl_per_season.png"),
        os.path.join("output", "top_defending_teams.png"),
        os.path.join("output", "top_chasing_teams.png"),
        os.path.join("output", "best_venues_defending.png"),
        os.path.join("output", "best_venues_chasing.png"),
        os.path.join("output", "rohit_season_performance.png"),
        os.path.join("output", "rohit_team_performance.png"),
        os.path.join("output", "rohit_dismissal_patterns.png"),
        os.path.join("output", "rohit_phase_performance.png"),
        os.path.join("output", "rohit_innings_performance.png"),
        os.path.join("output", "rohit_consistency_analysis.png"),
        os.path.join("output", "rohit_venue_performance.png"),
        os.path.join("output", "rohit_milestones.png")
    ]
    
    # Filter only existing visualization files
    existing_viz_paths = [path for path in visualization_paths if os.path.exists(path)]
    
    pdf_path = report_generator.generate_comprehensive_report(analysis_results, existing_viz_paths)
    txt_path = report_generator.generate_text_report(analysis_results)
    
    # Generate Rohit Sharma specific reports
    print("\n7. Generating Rohit Sharma specific reports...")
    rohit_viz_paths = [path for path in existing_viz_paths if 'rohit' in path]
    rohit_pdf_path = rohit_report_generator.generate_rohit_sharma_report(rohit_analysis, rohit_viz_paths)
    rohit_txt_path = rohit_report_generator.generate_rohit_text_report(rohit_analysis)
    
    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE!")
    print("Visualizations saved to 'output' directory")
    print(f"Main PDF Report: {pdf_path}")
    print(f"Main Text Report: {txt_path}")
    print(f"Rohit Sharma PDF Report: {rohit_pdf_path}")
    print(f"Rohit Sharma Text Report: {rohit_txt_path}")
    print("=" * 60)


if __name__ == "__main__":
    main()
