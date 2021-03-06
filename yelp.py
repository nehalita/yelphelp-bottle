"""Interface to the Yelp Search API."""

import json
import optparse
import urllib
import urllib2
import oauth2

def request(host, path, url_params, consumer_key, consumer_secret, token, token_secret):
  """
  Returns response for API request.
  """
  # Unsigned URL
  encoded_params = ''
  if url_params:
    encoded_params = urllib.urlencode(url_params)
  url = 'http://%s%s?%s' % (host, path, encoded_params)
  print 'URL: %s' % (url,)

  # Sign the URL
  consumer = oauth2.Consumer(consumer_key, consumer_secret)
  oauth_request = oauth2.Request('GET', url, {})
  oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
                        'oauth_timestamp': oauth2.generate_timestamp(),
                        'oauth_token': token,
                        'oauth_consumer_key': consumer_key})

  token = oauth2.Token(token, token_secret)
  oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
  signed_url = oauth_request.to_url()
  print 'Signed URL: %s\n' % (signed_url,)

  # Connect
  try:
    conn = urllib2.urlopen(signed_url, None)
    try:
      response = json.loads(conn.read())
    finally:
      conn.close()
  except urllib2.HTTPError, error:
    response = json.loads(error.read())

  return response


CONSUMER_KEY    = "4tJuC_cohWepkmlK2_dqBg"
CONSUMER_SECRET = "ktEsc1P6jE1Oui_GLghs6pP_kZ0"
TOKEN           = "Ep2czF2gK5B3aYnhyg5n9e9IxE7kXEfY"
TOKEN_SECRET    = "B2Z2kfQYZKuElmavomhmZskujXs"

MAX_RESTAURANTS = 10

def search_yelp(search_term, latitude, longitude):

    lat_long_str = "%f,%f" % (latitude, longitude)
    searchParams = {
        'term': search_term,
        'll': lat_long_str,
        'limit': MAX_RESTAURANTS,
    }
    response = request(
        'api.yelp.com',
        '/v2/search',
        searchParams,
        CONSUMER_KEY,
        CONSUMER_SECRET,
        TOKEN,
        TOKEN_SECRET)
    return response

def get_yelp_business(businessId):
  biz_url = "/v2/business/%s" % businessId
  response = request(
      'api.yelp.com',
      biz_url,
      None,
      CONSUMER_KEY,
      CONSUMER_SECRET,
      TOKEN,
      TOKEN_SECRET)
  return response
