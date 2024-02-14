-- Lists all the cities of California that can be found in database hbtn_od_usa
SELECT id, name FROM cities WHERE state_id = (
	SELECT id
	FROM states
	Where name = "California");
