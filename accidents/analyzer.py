import geopandas as gpd
import matplotlib.pyplot as plt

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

        from sklearn.preprocessing import MinMaxScaler
        scaler = MinMaxScaler()
        state_stats[['Rate_Norm', 'Severity_Norm']] = scaler.fit_transform(
            state_stats[['Accident_Rate', 'Avg_Severity']]
        )
        state_stats['Composite_Risk_Score'] = (
            0.5 * state_stats['Rate_Norm'] + 0.5 * state_stats['Severity_Norm']
        )

        self.state_stats = state_stats.reset_index().rename(columns={'State': 'State_Code'})
        return self.state_stats

    def export_to_csv(self, filepath='state_risk_scores.csv'):
        if self.state_stats is not None:
            self.state_stats.to_csv(filepath, index=False)
        else:
            raise ValueError("Run compute_risk_scores() first.")

    def plot_risk_map(self, metric='Composite_Risk_Score', cmap='OrRd', save_path=None):
        if self.state_stats is None:
            raise ValueError("Run compute_risk_scores() first.")
        
        # Load US states GeoJSON
        geojson_url = 'https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json'
        gdf = gpd.read_file(geojson_url)

        # Merge on state name
        state_abbrev_to_name = {
            'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California',
            'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia',
            'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa',
            'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
            'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi', 'MO': 'Missouri',
            'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire', 'NJ': 'New Jersey',
            'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina', 'ND': 'North Dakota', 'OH': 'Ohio',
            'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania', 'RI': 'Rhode Island', 'SC': 'South Carolina',
            'SD': 'South Dakota', 'TN': 'Tennessee', 'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont',
            'VA': 'Virginia', 'WA': 'Washington', 'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming', 'DC': 'District of Columbia'
        }

        self.state_stats['State_Name'] = self.state_stats['State_Code'].map(state_abbrev_to_name)
        merged = gdf.merge(self.state_stats, left_on='name', right_on='State_Name')

        # Plot
        fig, ax = plt.subplots(1, 1, figsize=(15, 10))
        merged.plot(column=metric, cmap=cmap, linewidth=0.8, edgecolor='0.8',
                    legend=True, ax=ax)
        ax.set_title(f'{metric.replace("_", " ")} by State', fontsize=16)
        ax.axis('off')

        if save_path:
            plt.savefig(save_path, bbox_inches='tight')
        plt.show()
