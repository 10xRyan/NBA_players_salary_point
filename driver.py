from extractor import scrap
import pandas as pd

class getSalary:
    def get(self):
        url_list=["https://www.spotrac.com/nba/rankings/earnings/2023/center/active/",
                "https://www.spotrac.com/nba/rankings/earnings/2023/point-guard/active/",
                "https://www.spotrac.com/nba/rankings/earnings/2023/shooting-guard/active/",
                "https://www.spotrac.com/nba/rankings/earnings/2023/small-forward/active/",
                "https://www.spotrac.com/nba/rankings/earnings/2023/power-forward/active/"]

        salary_df=pd.DataFrame(columns=['Player','EarningsTotal'])

        for i in url_list:
            df=scrap(i)
            salary_df=pd.concat([salary_df,df])

        salary_df.to_csv("artifacts/salary.csv",index=False,header=True)

if __name__=="__main__":
    obj=getSalary()
    obj.get()