# MedievalGame

Meanings:
() - create a instance in that class
no() - put some instance already create in that class

Logic:
World()     |Field()
            |Player()	|Coin
		    |           |Village()  |Population(Resource)
            |           |           |Resource(Mine, Storage, HidingPlace, Market)
            |           |           |Villager(Farm)
		    |		    |		    |MainBuilding(Village)
            |           |           |Mine(Village)
            |           |		    |Storage(Village)
            |           |           |HidingPlace(Village)
            |           |           |Market(Village)
		    |           |           |Farm(Village)
		    |           |           |Academy(Village)    |Coin()
		    |		    |		    |RallyPoint(Village)   |Army()
		    |           |           |                       |Campaign()
		    |           |           |Statue(Village)
		    |		    |		    |Military(Village)  |Soldier()    |Weapon
		    |		    |		    |		    	    |Shield
		    |		    |		    |		    		|Engine
		    |		    |		    |Smithy(Village)     |Weapon()
		    |           |           |WatchTower(Village)
		    |           |           |Wall(Village)
		    |		    |		    |Battle()   |Forces()
            |           |           |Army
		    |		    |
            |Battle

Presentation()  |Resources()
			    |Menu() |Overview() |Player
				|		|           |Village
			    |		|Buildings()    |Header()
			    |		|			    |Fill()     |Planet
			    |		|Market()     |Resources
			    |		|Military()
			    |		|RallyPoint()
			    |		|World()
			            |Tribe()
