Feature: SWAPI people
    Scenario Outline: Verify people
      When I am making request I am getting right name, birth_year and, and status_code
      Examples:
        |        name       | birth_year |     url      | status_code |
        |  Luke Skywalker   |  19BBY     |  people/1/   |    200      |
        |  C-3PO            |  112BBY    |  people/2/   |    200      |
        |  R2-D2            |  33BBY     |  people/3/   |    200      |
        |  Darth Vader      |  41.9BBY   |  people/4/   |    200      |
        |  Leia Organa      |  19BBY     |  people/5/   |    200      |