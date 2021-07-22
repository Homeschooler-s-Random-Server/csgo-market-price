# CS:GO Knife Price Prediction

Currently in active development

## Notes for development

1. Do not commit or push directly to `master`, but create your own branch:
  `git checkout -b your_branch`
2. You can then later submit your changes by making a pull request to `master`. We can then peer review the changes.

This is to prevent conflicts and make the workflow smoother.

## Variable
- Knife Type (Navaja, Gut, Bayonet, Classic, etc)
- StatTrak (Yes or Not)
- Skins (Vanilla, Scorched, Fade, Crimson Web, etc)
- Wear Rating (Factory New, Field Tested, etc)
- Float (integer from 0 to 1, can be categorized to wear rating)


## There's two output option (depend from which site the data scraped):
1. Steam Market Price (in dollar)
2. Price (in dollar) if you buy it using 3rd party website (skin baron, skinport, cs money)
