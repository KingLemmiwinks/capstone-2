-- test user has the password "password"

\c capstone_2_db

INSERT INTO users (username, password, first_name, last_name, email, phone_number)
VALUES ('testuser',
        '$2b$12$AZH7virni5jlTTiGgEg4zu3lSvAw68qVEfSIOjJ3RqtbJbdW/Oi5q',
        'Test',
        'User',
        'testuser@testuser.com',
        1234567890);

INSERT INTO households (street_address, city, state, zip, photo, notes)
VALUES ('123 Test rd', 
        'Testcity', 
        'Teststate', 
        '12345', 
        null, 
        'Test notes');

INSERT INTO "sellerExpertise" ("hasExpertise", "isLandlord", "isRealEstateLicensee", notes)
VALUES (TRUE,
        FALSE,
        FALSE,
        'Test notes');

INSERT INTO "ownershipOccupancy" ("mostRecentOccupation", "isOccupiedBySeller", "sellerOccupancyHistory", "hasHadPets", "purchaseDate", notes)
VALUES (NOW(),
        FALSE,
        NULL,
        FALSE,
        NOW(),
        NULL
        );

INSERT INTO "roleTypes"("roleTypeName")
 VALUES ('The Owner'),
        ('The Executor'),
        ('The Administrator'),
        ('The Trustee'),
        ('An Individual Holding Power of Attorney');

INSERT INTO associations (fees, "initiationFees", "communityMaintenance", notes)
VALUES (NULL,
        NULL,
        NULL,
        'Test notes');

INSERT INTO "associationTypes"("associationTypeName")
    VALUES  ('Condomunium'),
            ('H.O.A.'),
            ('Cooperative');

INSERT INTO "frequencyTypes"("frequencyTypeName")
    VALUES  ('Monthly'),
            ('Quarterly'),
            ('Yearly');

INSERT INTO roof ("installationDate", "invoicePhoto", "hasBeenReplaced", "hadExistingMaterialRemoved", "hasPreexistingLeaks", "hasRainwaterProblems", notes)
VALUES (NOW(),
        NULL,
        TRUE,
        FALSE,
        FALSE,
        FALSE,
        'Test notes');

INSERT INTO basements ("hasSumpPump", "pumpCount", "hasBeenUsed", "hasWaterDamage", "hasRepairs", "hasDownspoutConnection", notes)
VALUES (TRUE,
        1,
        TRUE,
        FALSE,
        FALSE,
        True,
        'Test notes');
