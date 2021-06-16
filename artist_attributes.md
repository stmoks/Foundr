# Artist attributes

Each of the artists requires various attributes to go with their container. I've found that spotify
has a few that could prove useful. Below is a list of such attributes and their use in the creation
of Foundr. 

**Questions**
1. How do we create tables and databases that efficiently add new attributes/metrics?
2. For the creator products or channels, how do we scale that? New table or just an addition to a table?


## Artist
    - artist id
    - post id
    - text id
    - type
    - uri
    - languages
    - url
    - feed id
    - licence id
    - portfolio id
    - message id
    - mentions
    - awards
    - name
    - gender
    - inspired by
    - DOB
    - location
    - prospectus (summary or intro video)
    - country
    - genres
    - date joined
    - instruments
    - followers
    - following
    - playlist/bookmark
    - investors
    - social media accounts / websites
    - images
    - total creation time
    - share price
    - email
    - password
    - sponsors/endorsements
    

## Album
    - album id
    - artist ids
    - uri
    - url
    - languages
    - https
    - type
    - artist id
    - song id
    - description
    - cover picture
    - release date
    - ranking/popularity

## Associated acts
    - artist id

## Song
    - song id
    - isrc
    - artist ids
    - uri
    - album
    - url
    - https
    - type
    - languages
    - track number
    - licence id
    - description
    - artist id
    - release date
    - duration
    - bpm
    - subscriptions (groups around an idea/genre)
    - cover image
    - title
    - writer
    - lyrics
    - track 
    - play/listen count
    - rating/ranking/popularity
    - comments

## Market indicators
    - artist id
    - year started
    - followers
    - investors

## Events
    - artist id
    - event id
    - description
    - location
    - cover image
    - social media
    - link

## General media container
    - artist id
    - media item

## Portfolio
    - portfolio id
    - funds
    - total earnings
    - shareholding
    - currency

## Feed
    - artist id
    - item
    - comments
    - likes

## Messages
    - artist id
    - message id
    - messages
    - user id
    - media link

## Subscriptions
    - subscription id
    - content
    - artist ids