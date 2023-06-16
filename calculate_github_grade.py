#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
Calculate the grade on github according to the github-readme-stats
https://github-readme-stats.vercel.app/api?username=GITHUB_USERNAME&count_private=false&show_icons=true&theme=chartreuse-dark&PAT_1
eg: https://github-readme-stats.vercel.app/api?username=madhav-mknc&count_private=false&show_icons=true&theme=chartreuse-dark&PAT_1
algorithm: https://github.com/anuraghazra/github-readme-stats/blob/master/src/calculateRank.js
"""

def exponential_cdf(x):
    return 1-(2**(-x))

def log_normal_cdf(x):
    return x/(1+x)


def calculateRank(all_commits, commits, prs, issues, stars, followers):

    COMMITS_MEDIAN = 1000 if all_commits else 250
    COMMITS_WEIGHT = 2

    PRS_MEDIAN = 50
    PRS_WEIGHT = 3

    ISSUES_MEDIAN = 25
    ISSUES_WEIGHT = 1

    STARS_MEDIAN = 50
    STARS_WEIGHT = 4
    
    FOLLOWERS_MEDIAN = 10
    FOLLOWERS_WEIGHT = 1

    TOTAL_WEIGHT = COMMITS_WEIGHT + PRS_WEIGHT + ISSUES_WEIGHT + STARS_WEIGHT + FOLLOWERS_WEIGHT

    THRESHOLDS = [1, 12.5, 25, 37.5, 50, 62.5, 75, 87.5, 100]
    LEVELS = ["S", "A+", "A", "A-", "B+", "B", "B-", "C+", "C"]

    # calculated rank
    rank = 1 - (COMMITS_WEIGHT * exponential_cdf(commits/COMMITS_MEDIAN)
                + PRS_WEIGHT * exponential_cdf(prs/PRS_MEDIAN)
                + ISSUES_WEIGHT * exponential_cdf(issues/ISSUES_MEDIAN)
                + STARS_WEIGHT * log_normal_cdf(stars/STARS_MEDIAN)
                + FOLLOWERS_WEIGHT * log_normal_cdf(followers/FOLLOWERS_MEDIAN)) / TOTAL_WEIGHT
    # rank = float(input("Enter rank: "))

    level = LEVELS[THRESHOLDS.index(next(t for t in THRESHOLDS if rank * 100 <= t))]
    return f"\nlevel: {level}\npercentile: {100-rank*100}\n"


if __name__ == "__main__":
    # # params: all_commits, commits, prs, issues, repos, stars, followers
    # all_commits = True if input("[+] All commits? (Y/N) : ").lower()=='y' else False
    # commits = int(input("[+] Enter Commits: "))
    # prs = int(input("[+] Enter PRS: "))
    # issues = int(input("[+] Enter Issues: "))
    # repos = int(input("[+] Enter repos: ")) # unused
    # stars = int(input("[+] Enter stars: "))
    # followers = int(input("[+] Enter followers: "))

    while True:
        try:
            print("Enter: commits prs issues stars followers")
            inp = list(map(int, input("Enter: ").split())) 
            grade = calculateRank(True, *inp)

            # grade = calculateRank(all_commits, commits, prs, issues, repos, stars, followers)
            print("\n[*] Your Github Grade stats:", grade)
        except KeyboardInterrupt:
            break 
        except Exception:
            pass
