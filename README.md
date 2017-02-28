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
		    |		    |		    |Military(Villager, Weapon) |Soldier()    |Weapon
		    |		    |		    |		    			    |Shield
		    |		    |		    |		    			    |Engine
		    |		    |		    |RallyPoint()   |Army()
		    |           |           |               |Campaign()
		    |		    |		    |Smithy()     |Weapon()
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
			            |Statue()
