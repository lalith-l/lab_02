import requests
import pandas as pd

def fetch_remoteok_jobs():
    api_url = "https://remoteok.com/api"
    
    print("Fetching job data from RemoteOK...")

    try:
        response = requests.get(api_url)
        response.raise_for_status() 
        job_listings = response.json()[1:]
        print(f"✅ Successfully fetched {len(job_listings)} job listings.")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching data: {e}")
        return

    processed_jobs = []
    for job in job_listings:
        processed_jobs.append({
            "Company Name": job.get('company'),
            "Job Role": job.get('position'),
            "Location": job.get('location'),
            "Features or Tags": ", ".join(job.get('tags', []))
        })
    
    column_order = ["Company Name", "Job Role", "Location", "Features or Tags"]
    df = pd.DataFrame(processed_jobs, columns=column_order)

    output_filename = "remoteok_jobs.csv"
    df.to_csv(output_filename, index=False)
    
    print(f"\n✨ Data extraction complete! Saved to '{output_filename}'")
    
    print("\nHere's a preview of your data:")
    for index, row in df.head().iterrows():
        print(f"Company Name:     {row['Company Name']}")
        print(f"Job Role:         {row['Job Role']}")
        print(f"Location:         {row['Location']}")
        print(f"Features or Tags: {row['Features or Tags']}")
        print("-" * 40)

if __name__ == "__main__":
    fetch_remoteok_jobs()