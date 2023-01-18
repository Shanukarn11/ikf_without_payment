BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "registration_mastergroup" (
	"id"	integer NOT NULL,
	"group"	varchar(300),
	"start"	date NOT NULL,
	"end"	date NOT NULL,
	"gender"	varchar(100) NOT NULL,
	"year"	varchar(300),
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "registration_mastergroup" ("id","group","start","end","gender","year","include","orderid") VALUES (1,'Under 13','2009-01-01','2014-01-01','Male','2022',0,1),
 (2,'Under 15','2007-01-01','2009-01-02','Male','2022',1,2),
 (3,'Under 17','2005-01-01','2007-01-02','Male','2022',1,3),
 (4,'Under 16','2006-01-01','2014-01-02','Female','2022',1,4),
 (5,'Under 18','2004-01-01','2006-01-02','Female','2022',1,5);
CREATE INDEX IF NOT EXISTS "registration_mastergroup_group_ada7c02d" ON "registration_mastergroup" (
	"group"
);
CREATE INDEX IF NOT EXISTS "registration_mastergroup_start_ce0703f8" ON "registration_mastergroup" (
	"start"
);
CREATE INDEX IF NOT EXISTS "registration_mastergroup_end_f716c6dd" ON "registration_mastergroup" (
	"end"
);
CREATE INDEX IF NOT EXISTS "registration_mastergroup_gender_9f87d01e" ON "registration_mastergroup" (
	"gender"
);
CREATE INDEX IF NOT EXISTS "registration_mastergroup_year_49a0cd5f" ON "registration_mastergroup" (
	"year"
);
COMMIT;
