define({ api: [
  {
    "type": "get",
    "url": "/api/clubs/:id",
    "title": "Request club information",
    "name": "GetClub",
    "group": "Club",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "Club unique id"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "field": "name",
            "optional": false,
            "description": "Club name"
          },
          {
            "group": "Success 200",
            "type": "String",
            "field": "address",
            "optional": false,
            "description": "Club address"
          },
          {
            "group": "Success 200",
            "type": "String",
            "field": "contact",
            "optional": false,
            "description": "Club contact details"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./bowls/clubs/api.py"
  },
  {
    "type": "get",
    "url": "/api/clubs/",
    "title": "Request a list of Clubs",
    "name": "ListClubs",
    "group": "Club",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Object[]",
            "field": "clubs",
            "optional": false,
            "description": "List of clubs"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./bowls/clubs/api.py"
  },
  {
    "type": "get",
    "url": "/api/players/:id",
    "title": "Request Player information",
    "name": "GetPlayer",
    "group": "Player",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "Player unique id"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "field": "name",
            "optional": false,
            "description": "Player name"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./bowls/clubs/api.py"
  },
  {
    "type": "get",
    "url": "/api/players/",
    "title": "Request a list of Players",
    "name": "ListPlayers",
    "group": "Player",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Object[]",
            "field": "players",
            "optional": false,
            "description": "List of Players"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./bowls/clubs/api.py"
  },
  {
    "type": "get",
    "url": "/api/teams/:id",
    "title": "Request team information",
    "name": "GetTeam",
    "group": "Team",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "field": "id",
            "optional": false,
            "description": "Team unique id"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "String",
            "field": "name",
            "optional": false,
            "description": "Team name"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./bowls/clubs/api.py"
  },
  {
    "type": "get",
    "url": "/api/teams/",
    "title": "Request a list of Teams",
    "name": "ListTeams",
    "group": "Team",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Object[]",
            "field": "teams",
            "optional": false,
            "description": "List of teams"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "./bowls/clubs/api.py"
  }
] });