# MedievalGame

Meanings:
() - create a instance in that class
no() - put/use some instance already create in that class

Logic:
World()     |Continent()    |Zone() |Village()
            |Field()
            |Player()	|Village    |Population()   |Villagers()    |Villager
            |           |           |               |Units()    |Unit
            |           |           |Resources()    |Resource
            |           |           |Buildings()    |MainBuilding()
            |           |           |               |Farm() |Villager()
		    |		    |		    |               |Mine()     |Resource()
            |           |           |               |HidingPlace()
            |           |		    |               |Storage()
            |           |           |               |Market()
		    |           |           |               |Academy()  |Coin()
		    |		    |		    |               |RallyPoint()   |Army()
		    |           |           |               |               |Campaign()
		    |           |           |               |Statue()
		    |		    |		    |               |Barracks()  |Unit()    |Weapon
		    |		    |		    |               |		    	        |Shield
		    |		    |		    |               |		    		    |Engine
		    |		    |		    |               |Smithy()   |Weapon()
		    |		    |		    |               |		    |Shield()
		    |		    |		    |               |		    |Engine()
		    |           |           |               |WatchTower()
		    |           |           |               |Wall()
		    |		    |		    |Battle()   |Forces()   |Units
            |           |           |           |           |WatchTower
		    |           |           |           |           |Wall
            |           |           |           |Army
		    |		    |Coin


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
