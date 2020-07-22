# NLP ANalysis on Reddit Posts & Comments
Examining the features of Reddit's PRAW (Python Reddit API Wrapper) and analysis of posts &amp; comments

## Getting Started
1. Clone this repo
2. Obtain Reddit API credentials

### Credfile
These notebooks reference a JSON credfile to authenticate with your Reddit account. You can get these credentials from your reddit account, or follow the Ppraw documnetation [here](https://praw.readthedocs.io/en/latest/getting_started/quick_start.html). The credfile is stored in the same direcotry as the notebooks, and looks as follows:

```
{
	"client_id" : "your_client_id",
	"client_secret": "your_client_secret",
	"user_agent": "choose_user_agent_name"
}
```