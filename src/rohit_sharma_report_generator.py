"""
Rohit Sharma Career Analysis Report Generator

This module generates comprehensive reports specifically focused on 
Rohit Sharma's IPL career performance and insights.
"""

import os
from datetime import datetime
from typing import Dict, List
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors


class RohitSharmaReportGenerator:
    """Generates detailed reports for Rohit Sharma's career analysis."""
    
    def __init__(self, output_dir: str = "output"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()
    
    def _setup_custom_styles(self):
        """Setup custom paragraph styles for the report."""
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            textColor=colors.darkblue,
            alignment=1  # Center alignment
        ))
        
        self.styles.add(ParagraphStyle(
            name='CustomHeading',
            parent=self.styles['Heading2'],
            fontSize=16,
            spaceAfter=12,
            textColor=colors.darkgreen
        ))
        
        self.styles.add(ParagraphStyle(
            name='CustomSubheading',
            parent=self.styles['Heading3'],
            fontSize=14,
            spaceAfter=10,
            textColor=colors.darkred
        ))
    
    def generate_rohit_sharma_report(self, rohit_analysis: Dict, 
                                    visualization_paths: List[str] = None) -> str:
        """Generate comprehensive PDF report for Rohit Sharma's career analysis."""
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"rohit_sharma_career_analysis_{timestamp}.pdf"
        filepath = os.path.join(self.output_dir, filename)
        
        doc = SimpleDocTemplate(filepath, pagesize=A4)
        story = []
        
        # Title Page
        self._add_title_page(story)
        
        # Executive Summary
        self._add_executive_summary(story, rohit_analysis)
        
        # Career Overview
        self._add_career_overview(story, rohit_analysis)
        
        # Performance Analysis
        self._add_performance_analysis(story, rohit_analysis)
        
        # Season-wise Analysis
        self._add_season_analysis(story, rohit_analysis)
        
        # Team Performance
        self._add_team_performance(story, rohit_analysis)
        
        # Phase-wise Performance
        self._add_phase_performance(story, rohit_analysis)
        
        # Consistency Analysis
        self._add_consistency_analysis(story, rohit_analysis)
        
        # Milestones and Records
        self._add_milestones(story, rohit_analysis)
        
        # Visualizations (if available)
        if visualization_paths:
            self._add_visualizations(story, visualization_paths)
        
        # Key Insights and Recommendations
        self._add_insights(story, rohit_analysis)
        
        doc.build(story)
        return filepath
    
    def _add_title_page(self, story: List):
        """Add title page to the report."""
        story.append(Spacer(1, 2*inch))
        story.append(Paragraph("ROHIT SHARMA", self.styles['CustomTitle']))
        story.append(Paragraph("IPL Career Analysis Report", self.styles['CustomTitle']))
        story.append(Spacer(1, 1*inch))
        story.append(Paragraph(f"Generated on: {datetime.now().strftime('%B %d, %Y')}", 
                               self.styles['Normal']))
        story.append(Paragraph("Comprehensive Performance Analysis & Career Insights", 
                               self.styles['Normal']))
        story.append(PageBreak())
    
    def _add_executive_summary(self, story: List, rohit_analysis: Dict):
        """Add executive summary section."""
        story.append(Paragraph("Executive Summary", self.styles['CustomHeading']))
        
        career_span = rohit_analysis['career_span']
        basic_stats = rohit_analysis['basic_stats']
        milestones = rohit_analysis['milestones']
        
        summary_text = f"""
        This comprehensive analysis examines Rohit Sharma's IPL career spanning {career_span['total_seasons']} seasons 
        from {career_span['seasons'][0]} to {career_span['seasons'][-1]}. During this period, Rohit has established 
        himself as one of the most successful batsmen in IPL history.
        
        <b>Key Career Statistics:</b><br/>
        • Total Matches: {career_span['total_matches']}<br/>
        • Total Runs Scored: {basic_stats['total_runs']:,}<br/>
        • Batting Average: {basic_stats['average']}<br/>
        • Strike Rate: {basic_stats['strike_rate']}<br/>
        • Centuries: {milestones['centuries']}<br/>
        • Half-centuries: {milestones['half_centuries']}<br/>
        • Man of Match Awards: {rohit_analysis['captaincy']['mom_awards']}
        """
        
        story.append(Paragraph(summary_text, self.styles['Normal']))
        story.append(Spacer(1, 0.3*inch))
    
    def _add_career_overview(self, story: List, rohit_analysis: Dict):
        """Add career overview section."""
        story.append(Paragraph("Career Overview", self.styles['CustomHeading']))
        
        # Create career statistics table
        career_data = [
            ['Metric', 'Value'],
            ['Career Span', f"{rohit_analysis['career_span']['seasons'][0]} - {rohit_analysis['career_span']['seasons'][-1]}"],
            ['Seasons Played', str(rohit_analysis['career_span']['total_seasons'])],
            ['Total Matches', str(rohit_analysis['career_span']['total_matches'])],
            ['Total Runs', f"{rohit_analysis['basic_stats']['total_runs']:,}"],
            ['Total Balls Faced', f"{rohit_analysis['basic_stats']['total_balls']:,}"],
            ['Batting Average', f"{rohit_analysis['basic_stats']['average']}"],
            ['Strike Rate', f"{rohit_analysis['basic_stats']['strike_rate']}"],
            ['Centuries', str(rohit_analysis['milestones']['centuries'])],
            ['Half-centuries', str(rohit_analysis['milestones']['half_centuries'])],
            ['Man of Match Awards', str(rohit_analysis['captaincy']['mom_awards'])]
        ]
        
        table = Table(career_data, colWidths=[3*inch, 2*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        story.append(table)
        story.append(Spacer(1, 0.3*inch))
    
    def _add_performance_analysis(self, story: List, rohit_analysis: Dict):
        """Add detailed performance analysis."""
        story.append(Paragraph("Performance Analysis", self.styles['CustomHeading']))
        
        # Dismissal Analysis
        story.append(Paragraph("Dismissal Patterns", self.styles['CustomSubheading']))
        dismissal_data = [['Dismissal Type', 'Count']]
        for dismissal_type, count in rohit_analysis['dismissal_analysis'].items():
            dismissal_data.append([dismissal_type, str(count)])
        
        dismissal_table = Table(dismissal_data, colWidths=[3*inch, 1.5*inch])
        dismissal_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        story.append(dismissal_table)
        story.append(Spacer(1, 0.2*inch))
        
        # Innings Performance
        story.append(Paragraph("Innings-wise Performance", self.styles['CustomSubheading']))
        innings_perf = rohit_analysis['innings_performance']
        
        innings_text = f"""
        <b>1st Innings Performance:</b><br/>
        • Runs: {innings_perf['inning_1']['runs']}<br/>
        • Strike Rate: {innings_perf['inning_1']['strike_rate']}<br/>
        • Average: {innings_perf['inning_1']['average']}<br/><br/>
        
        <b>2nd Innings Performance:</b><br/>
        • Runs: {innings_perf['inning_2']['runs']}<br/>
        • Strike Rate: {innings_perf['inning_2']['strike_rate']}<br/>
        • Average: {innings_perf['inning_2']['average']}
        """
        
        story.append(Paragraph(innings_text, self.styles['Normal']))
        story.append(Spacer(1, 0.3*inch))
    
    def _add_season_analysis(self, story: List, rohit_analysis: Dict):
        """Add season-wise performance analysis."""
        story.append(Paragraph("Season-wise Performance", self.styles['CustomHeading']))
        
        season_data = [['Season', 'Matches', 'Runs', 'Average', 'Strike Rate']]
        season_perf = rohit_analysis['season_performance']
        
        # Sort seasons and take recent 8 seasons
        recent_seasons = sorted(season_perf.keys())[-8:]
        for season in recent_seasons:
            stats = season_perf[season]
            season_data.append([
                str(season),
                str(stats['matches']),
                str(stats['runs']),
                str(stats['average']),
                str(stats['strike_rate'])
            ])
        
        season_table = Table(season_data, colWidths=[1*inch, 1*inch, 1.2*inch, 1.2*inch, 1.2*inch])
        season_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        story.append(season_table)
        story.append(Spacer(1, 0.3*inch))
    
    def _add_team_performance(self, story: List, rohit_analysis: Dict):
        """Add team-wise performance analysis."""
        story.append(Paragraph("Team-wise Performance", self.styles['CustomHeading']))
        
        team_data = [['Team', 'Matches', 'Runs', 'Average', 'Strike Rate']]
        team_perf = rohit_analysis['team_performance']
        
        for team, stats in team_perf.items():
            team_data.append([
                team,
                str(stats['matches']),
                str(stats['runs']),
                str(stats['average']),
                str(stats['strike_rate'])
            ])
        
        team_table = Table(team_data, colWidths=[2*inch, 1*inch, 1.2*inch, 1.2*inch, 1.2*inch])
        team_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        story.append(team_table)
        story.append(Spacer(1, 0.3*inch))
    
    def _add_phase_performance(self, story: List, rohit_analysis: Dict):
        """Add phase-wise performance analysis."""
        story.append(Paragraph("Phase-wise Performance", self.styles['CustomHeading']))
        
        phase_data = [['Phase', 'Runs', 'Balls', 'Strike Rate', 'Average']]
        phase_perf = rohit_analysis['phase_performance']
        
        for phase, stats in phase_perf.items():
            phase_data.append([
                phase.title(),
                str(stats['runs']),
                str(stats['balls']),
                str(stats['strike_rate']),
                str(stats['average'])
            ])
        
        phase_table = Table(phase_data, colWidths=[1.5*inch, 1*inch, 1*inch, 1.2*inch, 1.2*inch])
        phase_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        story.append(phase_table)
        story.append(Spacer(1, 0.3*inch))
    
    def _add_consistency_analysis(self, story: List, rohit_analysis: Dict):
        """Add consistency analysis."""
        story.append(Paragraph("Consistency Analysis", self.styles['CustomHeading']))
        
        consistency = rohit_analysis['consistency']
        
        consistency_text = f"""
        <b>Statistical Consistency Metrics:</b><br/>
        • Mean Score: {consistency['mean_score']}<br/>
        • Median Score: {consistency['median_score']}<br/>
        • Standard Deviation: {consistency['std_deviation']}<br/>
        • Coefficient of Variation: {consistency['coefficient_of_variation']}%<br/><br/>
        
        <b>Score Distribution:</b><br/>
        • Total Innings: {consistency['total_innings']}<br/>
        • Scores Above 50: {consistency['scores_above_50']}<br/>
        • Scores Above 30: {consistency['scores_above_30']}<br/>
        • Ducks: {consistency['ducks']}
        """
        
        story.append(Paragraph(consistency_text, self.styles['Normal']))
        story.append(Spacer(1, 0.3*inch))
    
    def _add_milestones(self, story: List, rohit_analysis: Dict):
        """Add milestones and records section."""
        story.append(Paragraph("Career Milestones & Records", self.styles['CustomHeading']))
        
        milestones = rohit_analysis['milestones']
        
        # Top scores
        story.append(Paragraph("Highest Scores", self.styles['CustomSubheading']))
        high_scores = milestones['highest_scores'][:5]
        scores_text = ""
        for i, score in enumerate(high_scores, 1):
            scores_text += f"{i}. {score} runs<br/>"
        
        story.append(Paragraph(scores_text, self.styles['Normal']))
        story.append(Spacer(1, 0.2*inch))
        
        # Captaincy analysis
        story.append(Paragraph("Leadership Performance", self.styles['CustomSubheading']))
        captaincy = rohit_analysis['captaincy']
        
        captaincy_text = f"""
        • Man of Match Awards: {captaincy['mom_awards']}<br/>
        • Win Rate as Captain: {captaincy['win_rate_as_captain']}%<br/>
        • Total Leadership Impact: High
        """
        
        story.append(Paragraph(captaincy_text, self.styles['Normal']))
        story.append(Spacer(1, 0.3*inch))
    
    def _add_visualizations(self, story: List, visualization_paths: List[str]):
        """Add visualizations to the report."""
        story.append(Paragraph("Performance Visualizations", self.styles['CustomHeading']))
        
        rohit_viz_paths = [path for path in visualization_paths if 'rohit' in path]
        
        for viz_path in rohit_viz_paths:
            if os.path.exists(viz_path):
                try:
                    img = Image(viz_path, width=6*inch, height=4*inch)
                    story.append(img)
                    story.append(Spacer(1, 0.2*inch))
                except:
                    continue
        
        story.append(PageBreak())
    
    def _add_insights(self, story: List, rohit_analysis: Dict):
        """Add key insights and recommendations."""
        story.append(Paragraph("Key Insights & Analysis", self.styles['CustomHeading']))
        
        insights = self._generate_rohit_insights(rohit_analysis)
        
        for i, insight in enumerate(insights, 1):
            story.append(Paragraph(f"{i}. {insight}", self.styles['Normal']))
            story.append(Spacer(1, 0.1*inch))
    
    def _generate_rohit_insights(self, rohit_analysis: Dict) -> List[str]:
        """Generate specific insights about Rohit Sharma's performance."""
        insights = []
        
        basic_stats = rohit_analysis['basic_stats']
        milestones = rohit_analysis['milestones']
        consistency = rohit_analysis['consistency']
        
        # Strike rate insight
        if basic_stats['strike_rate'] > 130:
            insights.append("Excellent strike rate indicates aggressive batting approach, ideal for T20 format.")
        elif basic_stats['strike_rate'] > 120:
            insights.append("Good strike rate demonstrates ability to score quickly while maintaining consistency.")
        
        # Consistency insight
        if consistency['coefficient_of_variation'] < 80:
            insights.append("High consistency shown by low coefficient of variation, making him a reliable batsman.")
        
        # Milestone insight
        if milestones['centuries'] > 0:
            insights.append(f"Conversion of fifties to hundreds is impressive with {milestones['centuries']} centuries.")
        
        # Captaincy insight
        captaincy = rohit_analysis['captaincy']
        if captaincy['win_rate_as_captain'] > 50:
            insights.append("Strong leadership qualities evidenced by high win rate as captain.")
        
        # Phase performance insight
        phase_perf = rohit_analysis['phase_performance']
        if phase_perf['death']['strike_rate'] > 150:
            insights.append("Exceptional death overs performance shows ability to accelerate under pressure.")
        
        # Team performance insight
        team_perf = rohit_analysis['team_performance']
        if 'Mumbai Indians' in team_perf:
            insights.append("Long-term association with Mumbai Indians has contributed to team success and personal growth.")
        
        return insights
    
    def generate_rohit_text_report(self, rohit_analysis: Dict) -> str:
        """Generate text-based report for Rohit Sharma analysis."""
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"rohit_sharma_text_analysis_{timestamp}.txt"
        filepath = os.path.join(self.output_dir, filename)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("ROHIT SHARMA - IPL CAREER ANALYSIS REPORT\n")
            f.write("=" * 80 + "\n\n")
            f.write(f"Generated on: {datetime.now().strftime('%B %d, %Y %H:%M:%S')}\n\n")
            
            # Career Overview
            f.write("CAREER OVERVIEW\n")
            f.write("-" * 40 + "\n")
            career_span = rohit_analysis['career_span']
            basic_stats = rohit_analysis['basic_stats']
            
            f.write(f"Career Span: {career_span['seasons'][0]} - {career_span['seasons'][-1]}\n")
            f.write(f"Total Seasons: {career_span['total_seasons']}\n")
            f.write(f"Total Matches: {career_span['total_matches']}\n")
            f.write(f"Total Runs: {basic_stats['total_runs']:,}\n")
            f.write(f"Batting Average: {basic_stats['average']}\n")
            f.write(f"Strike Rate: {basic_stats['strike_rate']}\n\n")
            
            # Performance Analysis
            f.write("PERFORMANCE ANALYSIS\n")
            f.write("-" * 40 + "\n")
            milestones = rohit_analysis['milestones']
            f.write(f"Centuries: {milestones['centuries']}\n")
            f.write(f"Half-centuries: {milestones['half_centuries']}\n")
            f.write(f"Man of Match Awards: {rohit_analysis['captaincy']['mom_awards']}\n\n")
            
            # Season Performance
            f.write("RECENT SEASON PERFORMANCE\n")
            f.write("-" * 40 + "\n")
            season_perf = rohit_analysis['season_performance']
            recent_seasons = sorted(season_perf.keys())[-5:]
            
            for season in recent_seasons:
                stats = season_perf[season]
                f.write(f"{season}: {stats['runs']} runs @ {stats['strike_rate']} SR in {stats['matches']} matches\n")
            f.write("\n")
            
            # Key Insights
            f.write("KEY INSIGHTS\n")
            f.write("-" * 40 + "\n")
            insights = self._generate_rohit_insights(rohit_analysis)
            for i, insight in enumerate(insights, 1):
                f.write(f"{i}. {insight}\n")
        
        return filepath
