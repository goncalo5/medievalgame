# MedievalGame

Meanings:
() - create a instance in that class
no() - put some instance already create in that class

Logic:
World()     |Field()
            |Player()	|Coin
		    |           |Village()  |Resource(Mine, Storage, HidingPlace, Market)
            |           |           |Villager(Farm)
		    |		    |		    |MainBuilding(Building)
            |           |           |Mine()
            |           |		    |Storage()
            |           |           |HidingPlace()
            |           |           |Market()
		    |           |           |Farm()
		    |           |           |Academy()    |Coin()
		    |		    |		    |RallyPoint()   |Army()
		    |           |           |               |Campaign()
		    |           |           |Statue()
		    |		    |		    |Military(Villager, Weapon) |Soldier()    |Weapon
		    |		    |		    |		    			    |Shield
		    |		    |		    |		    			    |Engine
		    |		    |		    |Smithy()     |Weapon()
		    |           |           |WatchTower()
		    |           |           |Wall()
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
