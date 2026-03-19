# Day 5: Data Analysis with Pandas

Today, I dove into the Titanic dataset using Pandas, exploring patterns in survival, class, age, and more. The dataset is rich and really tells a story about who survived and who didn't.

## Key Takeaways

### Most Striking Finding

The thing that stood out most was the huge difference in survival between men and women. About **74% of women survived**, compared to only **19% of men**. Even within the same class, women were almost four times more likely to survive. It really drives home how strict the "women and children first" rule was during evacuation.

### Other Interesting Observations

- **Passenger class mattered a lot**: 1st class passengers had a survival rate of 63%, while 3rd class passengers were much lower at 24%
- **Children had a slight edge**: Those under 18 survived at 54%, higher than the overall average
- **Port of embarkation made a difference**: Passengers boarding at Cherbourg (C) had 55% survival, while those from Southampton (S) were only 34%
- **Cabin information is mostly missing**: Only about 23% of passengers have cabin data, so it's hard to draw conclusions from that alone

## What I'd Investigate Next

If I had more time, I'd explore:

1. **Family Dynamics**: Analyze survival rates by family size (combining SibSp and Parch) to see if traveling alone vs with family affected survival

2. **Fare Analysis**: Investigate the relationship between fare paid and survival, particularly within each passenger class

3. **Title Extraction**: Extract titles (Mr., Mrs., Miss., etc.) from names to see if social status affected survival beyond just passenger class

4. **Cabin Location**: For the 23% with cabin data, analyze if deck level or cabin location correlated with survival

The dataset reveals clear patterns of social hierarchy and emergency protocols that prioritized certain groups over others.
