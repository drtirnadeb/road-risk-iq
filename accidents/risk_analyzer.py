import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from sklearn.preprocessing import MinMaxScaler

class RiskAnalyzer:
    def __init__(self, df: pd.DataFrame, population_dict: dict):
        self.df = df
        self.population = population_dict
        self.state_stats = None

    def compute_risk_scores(self):
        grouped = self.df.groupby('State')
        state_stats = pd.DataFrame({
            'Accident_Count': grouped.size(),
            'Avg_Severity': grouped['Severity'].mean()
        })
        state_stats['Population'] = state_stats.index.map(self.population)
        state_stats.dropna(subset=['Population'], inplace=True)
        state_stats['Accident_Rate'] = (state_stats['Accident_Count'] / state_stats['Population']) * 100000

        scaler = MinMaxScaler()
        state_stats[['Rate_Norm', 'Severity_Norm']] = scaler.fit_transform(
            state_stats[['Accident_Rate', 'Avg_Severity']]
        )
        state_stats['Composite_Risk_Score'] = (
            0.5 * state_stats['Rate_Norm'] + 0.5 * state_stats['Severity_Norm']
        )

        self.state_stats = state_stats
        return state_stats

    def export_to_csv(self, filepath='state_risk_scores.csv'):
        if self.state_stats is not None:
            self.state_stats.to_csv(filepath)
        else:
            raise ValueError("Run compute_risk_scores() first.")

    def plot_risk_map(self, metric='Composite_Risk_Score', save_path='risk_map.html'):
        if self.state_stats is None:
            raise ValueError("Run compute_risk_scores() first.")

        geojson_url = 'https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json'
        state_stats = self.state_stats.copy()
        state_stats['State_Name'] = state_stats.index

        m = folium.Map(location=[37.8, -96], zoom_start=4)

        folium.Choropleth(
            geo_data=geojson_url,
            name=metric,
            data=state_stats,
            columns=['State_Name', metric],
            key_on='feature.properties.name',
            fill_color='YlOrRd',
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name=f'{metric} by State',
            nan_fill_color='gray'
        ).add_to(m)

        m.save(save_path)

    def plot_time_analysis(self, save_path=None):
        df = self.df.copy()
        df['Hour'] = pd.to_datetime(df['Start_Time']).dt.hour
        time_counts = df.groupby(['Hour', 'Severity']).size().unstack(fill_value=0)

        time_counts.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='viridis')
        plt.title('Accidents by Time of Day and Severity')
        plt.xlabel('Hour of Day')
        plt.ylabel('Number of Accidents')
        plt.xticks(rotation=0)
        plt.grid(axis='y', linestyle='--', alpha=0.6)
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=300)
        plt.show()

    def plot_weather_analysis(self, save_path=None):
        df = self.df.copy()
        weather_counts = df.groupby(['Weather_Condition', 'Severity']).size().unstack(fill_value=0)
        top_weather = weather_counts.sum(axis=1).sort_values(ascending=False).head(5).index
        top_weather_counts = weather_counts.loc[top_weather]

        top_weather_counts.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='Set2')
        plt.title('Accidents by Weather Condition and Severity (Top 5 Conditions)')
        plt.xlabel('Weather Condition')
        plt.ylabel('Number of Accidents')
        plt.xticks(rotation=45)
        plt.grid(axis='y', linestyle='--', alpha=0.6)
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=300)
        plt.show()
