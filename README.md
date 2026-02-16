# IPL Data Analysis Project

A comprehensive analysis of Indian Premier League (IPL) cricket data, providing insights into team performance, player statistics, venue analysis, and match patterns.

## Project Structure

```
ipl data/
├── data/                   # Raw CSV data files
│   ├── matches.csv        # Match-level data
│   └── deliveries.csv     # Ball-by-ball delivery data
├── src/                   # Source code modules
│   ├── __init__.py        # Package initialization
│   ├── data_loader.py     # Data loading and validation
│   ├── analyzer.py        # Statistical analysis functions
│   ├── visualizer.py      # Visualization utilities
│   └── report_generator.py # PDF and text report generation
├── output/                # Generated plots and reports
├── notebooks/             # Jupyter notebooks (optional)
├── main.py               # Main execution script
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Features

### Data Analysis
- **Match Statistics**: Win margins, team performance, venue analysis
- **Player Performance**: Man of the Match awards, six-hitting statistics
- **Toss Analysis**: Impact of toss decisions on match outcomes
- **Weather Impact**: Duckworth-Lewis method applications
- **Venue Characteristics**: Defending vs chasing performance by venue

### Visualizations
- Maximum run and wicket margin victories
- Matches per city distribution
- Team win statistics
- Toss decision distribution
- Top player performance charts
- D/L applications per season
- Defending and chasing team rankings
- Venue performance analysis

### Report Generation
- **PDF Reports**: Comprehensive analysis with embedded visualizations
- **Text Reports**: Detailed text-based analysis summaries
- **Executive Summaries**: Key insights and business recommendations
- **Data Overviews**: Dataset quality and completeness assessments

## Installation

1. Clone or download this project
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Run the complete analysis:
```bash
python main.py
```

This will:
- Load and analyze the IPL data
- Generate all visualizations
- Create a comprehensive PDF report
- Generate a text summary report

### Use individual modules:

```python
from src.data_loader import DataLoader
from src.analyzer import IPLAnalyzer
from src.visualizer import IPLVisualizer
from src.report_generator import ReportGenerator

# Load data
loader = DataLoader()
matches, deliveries = loader.load_data()

# Perform analysis
analyzer = IPLAnalyzer(matches, deliveries)
team_wins = analyzer.get_team_wins()

# Create visualizations
visualizer = IPLVisualizer()
visualizer.plot_team_wins(team_wins)

# Generate reports
report_generator = ReportGenerator()
analysis_results = {'team_wins': team_wins}
pdf_path = report_generator.generate_comprehensive_report(analysis_results)
```

## Output Files

### Visualizations (PNG format)
- `max_run_margin.png` - Highest run margin victory
- `max_wicket_margin.png` - Highest wicket margin victory
- `matches_per_city.png` - Match distribution by city
- `matches_won_by_team.png` - Team win statistics
- `toss_decision_distribution.png` - Toss decision pie chart
- `top_10_mom_players.png` - Man of Match awards leaderboard
- `top_10_six_hitters.png` - Six hitting statistics
- `dl_per_season.png` - Duckworth-Lewis applications by season
- `top_defending_teams.png` - Best defending teams
- `top_chasing_teams.png` - Best chasing teams
- `best_venues_defending.png` - Top venues for defending
- `best_venues_chasing.png` - Top venues for chasing

### Reports
- `ipl_analysis_report_YYYYMMDD_HHMMSS.pdf` - Comprehensive PDF report
- `ipl_analysis_text_YYYYMMDD_HHMMSS.txt` - Text-based summary report

## Data Sources

- `matches.csv`: Contains match-level information including teams, venues, winners, margins
- `deliveries.csv`: Contains ball-by-ball delivery data with batting and bowling statistics

## Key Insights

The analysis reveals several important patterns:
- Cities with higher match frequency indicate strong engagement potential
- Toss advantage exists but is not overwhelmingly decisive
- Certain teams dominate defending and chasing conditions
- Venue characteristics significantly impact match outcomes
- High six-hitting players contribute strongly to audience engagement

## Dependencies

- pandas: Data manipulation and analysis
- numpy: Numerical computing
- matplotlib: Plotting and visualization
- seaborn: Statistical data visualization
- reportlab: PDF generation

## Report Features

### PDF Report Sections
1. **Title Page** - Report metadata and generation timestamp
2. **Executive Summary** - Key findings and statistics overview
3. **Data Overview** - Dataset information and quality assessment
4. **Match Analysis** - Victory margins, toss impact, weather effects
5. **Team Performance** - Win statistics, venue performance
6. **Player Analysis** - Individual performance metrics
7. **Venue Analysis** - Geographic distribution and characteristics
8. **Business Insights** - Strategic recommendations
9. **Visualizations** - All generated charts and graphs

### Text Report Features
- Comprehensive analysis summary
- All key statistics and findings
- Business insights and recommendations
- Easy-to-read format for quick reference

## Contributing

Feel free to extend the analysis with additional metrics, visualizations, or statistical tests. The modular structure makes it easy to add new analysis functions to the `analyzer.py` module, new visualization types to `visualizer.py`, or customize report formats in `report_generator.py`.
