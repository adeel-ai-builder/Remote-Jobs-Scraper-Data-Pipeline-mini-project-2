from playwright.sync_api import sync_playwright
import pandas as pd 
import sqlite3

data=[]

with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://remoteok.com/remote-dev-jobs")
    page.wait_for_selector("tr.job")
    page.mouse.wheel(0, 5000)
    page.wait_for_timeout(3000)
    jobs=page.query_selector_all("tr.job")

    for job in jobs :
        title=job.query_selector("h2")
        company=job.query_selector("h3")
        link=job.query_selector("a")
        salary=job.query_selector(".salary")

        if title and company:
            title_text=title.inner_text().strip()
            company_text=company.inner_text().strip()

            if link:
                job_url="https://remoteok.com" + link.get_attribute("href")
            else:
                job_url="N/A"
            
            if salary:
                salary_text=salary.inner_text().strip()
            else:
                salary_text="Not Mentioned"
            
            data.append([title_text,company_text,salary_text,job_url,"RemoteOK"])

    browser.close()

df1=pd.DataFrame(data, columns=["Title","Company","Salary","Link","Source"])
df1.drop_duplicates(inplace=True)
df1=df1[df1["Title"]!=""]
df1.reset_index(drop=True, inplace=True)
df1.to_csv("professional_jobs.csv", index=False)

conn=sqlite3.connect("jobs_database.db")
df1.to_sql("jobs_table", conn, if_exists="replace", index=False)
conn.close()

print("Industry Level Job Scraping Completed Successfully 🚀")

