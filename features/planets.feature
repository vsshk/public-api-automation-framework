Feature: SWAPI planets
    Scenario: Verify planet Tatooine
        When I request for planet number "1"
        Then I getting planet name "Tatooine"

    Scenario: Verify planet Alderaan
        When I request for planet number "2"
        Then I getting planet name "Alderaan"

    Scenario: Verify planet Yavin IV
        When I request for planet number "3"
        Then I getting planet name "Yavin IV"

  Scenario: Verify planet Hoth
        When I request for planet number "4"
        Then I getting planet name "Hoth"
