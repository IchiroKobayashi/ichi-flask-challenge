import sys
import urllib
import tweepy
import webbrowser
sys.path.append('../')
import settings


def get_oauth_token(url: str) -> str:
    querys = urllib.parse.urlparse(url).query
    querys_dict = urllib.parse.parse_qs(querys)
    return querys_dict["oauth_token"][0]

if __name__ == '__main__':

    # Auth: Set Keys & Secrets for Twitter API
    auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_SECRET_KEY)

    try:
        # Generate Auth Page URL including oauth_token
        redirect_url = auth.get_authorization_url()
        print ("Redirect URL:", redirect_url)
    except tweepy.TweepError:
        print( "Error! Failed to get request token.")

    # Get oauth_token from the Redirect URL
    oauth_token = get_oauth_token(redirect_url)
    print("oauth_token:", oauth_token)

    # Set oauth_token to Request Token
    auth.request_token['oauth_token'] = oauth_token

    # Please confirm at twitter after login.
    webbrowser.open(redirect_url)

    # Copy & paste the verifier written in URL query parameter
    verifier = input("You can check Verifier on url parameter. Please input Verifier:")
    auth.request_token['oauth_token_secret'] = verifier

    try:
        # Get access token & secret
        auth.get_access_token(verifier)
    except tweepy.TweepError:
        print('Error! Failed to get access token.')

    print("access token key:", auth.access_token)
    print("access token secret:", auth.access_token_secret)

    # Output access token & secret into text file
    with open("../text/auth.text", mode="w") as f:
        text = "key: {}\nsecret: {}".format(auth.access_token, auth.access_token_secret)
        f.write(text)

    print("DONE")
