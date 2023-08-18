\c capstone_2_db

DROP TABLE IF EXISTS "associationTypes";

CREATE TABLE "associationTypes" (
    id Int, SERIAL, PRIMARY KEY)
    associationTypeName text
);

INSERT INTO "associationTypes"("associationTypeName")
    VALUES  ('Condomunium'),
            ('H.O.A.'),
            ('Cooperative');

DROP TABLE IF EXISTS "frequencyTypes";

CREATE TABLE "frequencyTypes" (
    id Int, SERIAL, PRIMARY KEY)
    associationTypeName text
);

INSERT INTO "frequencyTypes"("frequencyTypeName")
    VALUES  ('Monthly'),
            ('Quarterly'),
            ('Yearly');

DROP TABLE  IF EXISTS "roleTypes";

CREATE TABLE "roleTypes" (
    id Int, SERIAL, PRIMARY KEY)
    associationTypeName text
);

    INSERT INTO "roleTypes"("roleTypeName")
    VALUES  ('The Owner'),
            ('The Executor'),
            ('The Administrator'),
            ('The Trustee'),
            ('An Individual Holding Power of Attorney');