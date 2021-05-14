# Artist attributes

Each of the artists requires various attributes to go with their container. I've found that spotify
has a few that could prove useful. Below is a list of such attributes and their use in the creation
of Foundr. 

**Questions**
1. How do we create tables and databases that efficiently add new attributes/metrics?
2. For the creator products or channels, how do we scale that? New table or just an addition to a table?


## Artist
    - id
    - name
    - gender
    - DOB
    - location
    - prospectus (summary or intro video)
    - country
    - genre
    - year
    - instruments
    - followers
    - following
    - playlist/bookmark
    - investors
    - social media accounts / websites
    - cover picture
    - total creation time
    - total earnings
    - share price
    - email
    - password
    - sponsors/endorsements
    - portfolio id

## Album
    - artist id
    - song id
    - description
    - cover picture

## Associated acts
    - artist id

## Song
    - song id
    - description
    - artist id
    - date added
    - duration
    - bpm
    - cover
    - title
    - writer
    - lyrics
    - track
    - track id 
    - play/listen count
    - rating
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
    - shareholding
