#!/usr/bin/env python3

import codecs
import random
import sys
import csv
from enum import Enum

DEFAULT_PROMPT = """Given the following lineage relationships:
{quiz_relations}
{quiz_question}
Select the correct answer:
{quiz_answers}
Enclose the selected answer number in the <ANSWER> tag, for example: <ANSWER>1</ANSWER>."""

male_names = [
    'James', 'Robert', 'John', 'Michael', 'David',
    'William', 'Richard', 'Joseph', 'Thomas', 'Christopher',
    'Charles', 'Daniel', 'Matthew', 'Anthony', 'Mark',
    'Donald', 'Steven', 'Andrew', 'Paul', 'Joshua',
    'Kenneth', 'Kevin', 'Brian', 'George', 'Timothy',
    'Ronald', 'Jason', 'Edward', 'Jeffrey', 'Ryan',
    'Jacob', 'Gary', 'Nicholas', 'Eric', 'Jonathan',
    'Stephen', 'Larry', 'Justin', 'Scott', 'Brandon',
    'Benjamin', 'Samuel', 'Gregory', 'Alexander', 'Patrick',
    'Frank', 'Raymond', 'Jack', 'Dennis', 'Jerry',
    'Tyler', 'Aaron', 'Jose', 'Adam', 'Nathan',
    'Henry', 'Zachary', 'Douglas', 'Peter', 'Kyle',
    'Noah', 'Ethan', 'Jeremy', 'Walter', 'Christian',
    'Keith', 'Roger', 'Terry', 'Austin', 'Sean',
    'Gerald', 'Carl', 'Harold', 'Dylan', 'Arthur',
    'Lawrence', 'Jordan', 'Jesse', 'Bryan', 'Billy',
    'Bruce', 'Gabriel', 'Joe', 'Logan', 'Alan',
    'Juan', 'Albert', 'Willie', 'Elijah', 'Wayne',
    'Randy', 'Vincent', 'Mason', 'Roy', 'Ralph',
    'Bobby', 'Russell', 'Bradley', 'Philip', 'Eugene',
    'Johnny', 'Caleb', 'Shawn', 'Travis', 'Louis',
    'Isaac', 'Phillip', 'Lucas', 'Luke', 'Craig',
    'Cameron', 'Victor', 'Carlos', 'Liam', 'Cody',
    'Jimmy', 'Danny', 'Luis', 'Todd', 'Martin',
    'Evan', 'Jackson', 'Joel', 'Nathaniel', 'Harry',
    'Alex', 'Dale', 'Howard', 'Adrian', 'Hunter',
    'Angel', 'Antonio', 'Allen', 'Ian', 'Rodney',
    'Curtis', 'Stanley', 'Chad', 'Aiden', 'Theodore',
    'Jayden', 'Tony', 'Fred', 'Isaiah', 'Derek',
    'Leonard', 'Julian', 'Jesus', 'Marcus', 'Jeffery',
    'Connor', 'Steve', 'Ernest', 'Glenn', 'Ricky',
    'Marvin', 'Frederick', 'Wesley', 'Owen', 'Francis',
    'Jeremiah', 'Troy', 'Norman', 'Dustin', 'Earl',
    'Oliver', 'Melvin', 'Jared', 'Calvin', 'Edwin',
    'Clarence', 'Lee', 'Randall', 'Mike', 'Shane',
    'Sebastian', 'Eddie', 'Wyatt', 'Carter', 'Gavin',
    'Leo', 'Corey', 'Jay', 'Miguel', 'Blake',
    'Ronnie', 'Levi', 'Barry', 'Alfred', 'Dean',
    'Dominic', 'Landon', 'Chase', 'Tommy', 'Manuel',
    'Oscar', 'Jon', 'Ray', 'Seth', 'Herbert',
    'Trevor', 'Leroy', 'Brett', 'Mitchell', 'Darrell',
    'Don', 'Erik', 'Devin', 'Bernard', 'Micheal',
    'Xavier', 'Clifford', 'Jerome', 'Cole', 'Bill',
    'Warren', 'Leon', 'Mario', 'Derrick', 'Chris',
    'Ricardo', 'Max', 'Colton', 'Alejandro', 'Marc',
    'Brent', 'Eli', 'Jorge', 'Jim', 'Francisco',
    'Ivan', 'Garrett', 'Alvin', 'Josiah', 'Brayden',
    'Gordon', 'Colin', 'Charlie', 'Andre', 'Cory',
    'Grant', 'Edgar', 'Clayton', 'Franklin', 'Carson',
    'Lloyd', 'Jake', 'Tristan', 'Bryce', 'Gene',
    'Parker', 'Nolan', 'Diego', 'Spencer', 'Tom',
    'Jeff', 'Vernon', 'Lewis', 'Aidan', 'Maurice',
    'Preston', 'Casey', 'Duane', 'Floyd', 'Ruben',
    'Grayson', 'Roberto', 'Glen', 'Gilbert', 'Micah',
    'Reginald', 'Eduardo', 'Hayden', 'Hector', 'Cooper',
    'Lance', 'Clyde', 'Javier', 'Darren', 'Elias',
    'Jaxon', 'Omar', 'Jimmie', 'Maxwell', 'Damian',
    'Miles', 'Everett', 'Fernando', 'Neil', 'Johnathan',
    'Tanner', 'Dan', 'Harvey', 'Nicolas', 'Mateo',
    'Brady', 'Karl', 'Darryl', 'Lester', 'Brendan',
    'Herman', 'Dakota', 'Andres', 'Allan', 'Hudson',
    'Lincoln', 'Pedro', 'Abraham', 'Andy', 'Asher',
    'Clinton', 'Milton', 'Bob', 'Raul', 'Kurt',
    'Roman', 'Emmanuel', 'Sam', 'Ayden', 'Lonnie',
    'Leonardo', 'Marshall', 'Harrison', 'Roland', 'Rafael',
    'Kaleb', 'Brad', 'Arnold', 'Dalton', 'Tim',
    'Jace', 'Johnnie', 'Ashton', 'Rick', 'Santiago',
    'Giovanni', 'Sergio', 'Collin', 'Tyrone', 'Jaden',
    'Ezra', 'Chester', 'Greg', 'Cecil', 'Brody',
    'Drew', 'Erick', 'Cesar', 'Jonah', 'Dwayne',
    'Bryson', 'Byron', 'Lorenzo', 'Guy', 'Marco',
    'Ross', 'Dwight', 'Armando', 'Mathew', 'Angelo',
    'Ramon', 'Elmer', 'Devon', 'Terrence', 'Shaun',
    'Jaime', 'Terrance', 'Easton', 'Nelson', 'Wade',
    'Ted', 'Kent', 'Freddie', 'Felix', 'Kirk',
    'Perry', 'Cristian', 'Caden', 'Ezekiel', 'Kaden',
    'Damon', 'Israel', 'Stuart', 'Jonathon', 'Kayden',
    'Dillon', 'Wallace', 'Dallas', 'Julius', 'Kristopher',
    'Daryl', 'Claude', 'Ben', 'Damien', 'Rickey',
    'Jaxson', 'Julio', 'Hugh', 'Sidney', 'Weston',
    'Alberto', 'Malcolm', 'Emmett', 'Donnie', 'Abel',
    'Gage', 'Simon', 'Dominick', 'Donovan', 'Braxton',
    'Axel', 'Clifton', 'Enrique', 'Silas', 'Ryder',
    'Malachi', 'Trenton', 'Fredrick', 'Sawyer', 'Kai',
    'Dave', 'Conner', 'Bennett', 'Arturo', 'Alfredo',
    'Bentley', 'Josue', 'Geoffrey', 'Gerard', 'Camden',
    'Alec', 'Gerardo', 'Rex', 'Elliott', 'Myles',
    'Zane', 'Luca', 'Joey', 'Darius', 'Jameson',
    'Colby', 'Chance', 'Willard', 'Greyson', 'Graham',
    'Beau', 'Kenny', 'Marcos', 'Virgil', 'Trent',
    'Maverick', 'Elliot', 'Kelvin', 'Neal', 'Declan',
    'Bryant', 'Kerry', 'Tucker', 'Morris', 'Lyle',
    'Rene', 'Rudy', 'Leland', 'Emanuel', 'Wendell',
    'Jasper', 'Dante', 'Noel', 'Garry', 'Malik',
    'Kaiden', 'Salvatore', 'Jude', 'Salvador', 'Ty',
    'Pablo', 'Orlando', 'Tyson', 'Emilio', 'Randolph',
    'Griffin', 'Braden', 'Roderick', 'Otis', 'August',
    'Amir', 'Dawson', 'Benny', 'Luther', 'Earnest',
    'Clark', 'Carlton', 'Lane', 'Ernesto', 'Grady',
    'Brooks', 'Brock', 'Sammy', 'Forrest', 'Maddox',
    'Fabian', 'Nick', 'Jermaine', 'Bennie', 'Skyler',
    'Cedric', 'Frankie', 'Loren', 'Rudolph', 'Quentin',
    'Lukas', 'Kingston', 'Ira', 'Hubert', 'Waylon',
    'Ismael', 'Trey', 'Zion', 'Alton', 'Corbin',
    'Saul', 'Jayce', 'Gustavo', 'Jalen', 'Myron',
    'Cayden', 'Alonzo', 'Edmund', 'Alfonso', 'Gael',
    'Jaylen', 'Nickolas', 'Ellis', 'Delbert', 'Junior',
    'Archie', 'Desmond', 'Keegan', 'Willis', 'Wilson',
    'Kameron', 'Reid', 'Homer', 'Rowan', 'Gregg',
    'Clay', 'Ron', 'Kyler', 'Horace', 'Terrell',
    'Drake', 'Xander', 'Demetrius', 'Moses', 'Wilbur',
    'Ryker', 'Chandler', 'Pete', 'Jayson', 'Sheldon',
    'Lowell', 'Dexter', 'Toby', 'Terence', 'Walker',
    'Harley', 'Esteban', 'Emiliano', 'Conrad', 'King',
    'Rodolfo', 'Jamal', 'Ken', 'Dane', 'Brennan',
    'Darin', 'Laurence', 'Hugo', 'Reed', 'Sylvester',
    'Milo', 'Joaquin', 'Sherman', 'Rylan', 'Roosevelt',
    'Marty', 'Jaiden', 'Sterling', 'Lamar', 'Kendrick',
    'Jakob', 'Clint', 'Mack', 'Maximus', 'Zackary',
    'Ali', 'Bradford', 'Rory', 'Cade', 'Blaine',
    'Teddy', 'Guillermo', 'Wilbert', 'Solomon', 'Rhett',
    'River', 'Marlon', 'Quinton', 'Felipe', 'Bret',
    'Zachery', 'Royce', 'Zachariah', 'Irvin', 'Moises',
    'Darrin', 'Finn', 'Adan', 'Ervin', 'Brantley',
    'Judah', 'Lionel', 'Cornelius', 'Davis', 'Randal',
    'Holden', 'Deandre', 'Tommie', 'Heath', 'Darrel',
    'Anderson', 'Carroll', 'Darnell', 'Tomas', 'Winston',
    'Gilberto', 'Stewart', 'Branden', 'Rocky', 'Barrett',
    'Cruz', 'Stephan', 'Zayden', 'Mickey', 'Amos',
    'Doyle', 'Will', 'Antoine', 'Conor', 'Rocco',
    'Freddy', 'Zander', 'Dewayne', 'Landen', 'Irving',
    'Dewey', 'Dick', 'Rodrigo', 'Quincy', 'Matteo',
    'Timmy', 'Van', 'Brenden', 'Jerald', 'Jonas',
    'Amari', 'Johnathon', 'Tobias', 'Jarrod', 'Rogelio',
    'Karter', 'Ramiro', 'Rufus', 'Paxton', 'Reuben',
    'Cash', 'Colt', 'Marquis', 'Vance', 'Louie',
    'Rolando', 'Darwin', 'Titus', 'Leonel', 'Lamont',
    'Cary', 'Elbert', 'Adriel', 'Kody', 'Cyrus',
    'Nikolas', 'Mauricio', 'Issac', 'Jase', 'Jarrett',
    'Dorian', 'Beckett', 'Doug', 'Noe', 'Khalil',
    'Monte', 'Merle', 'Thaddeus', 'Theo', 'Isiah',
    'Boyd', 'Romeo', 'Enzo', 'Tate', 'Jax',
    'Otto', 'Matt', 'Messiah', 'Caiden', 'Bert',
    'Gunner', 'Harlan', 'Percy', 'Archer', 'Buddy',
    'Keaton', 'Phoenix', 'Jefferson', 'Nathanael', 'Tristen',
    'Aden', 'Orville', 'Robbie', 'Rodger', 'Raphael',
    'Eldon', 'Wilfred', 'Remington', 'Maximiliano', 'Kade',
    'Kobe', 'Stefan', 'Jett', 'Kristian', 'Brendon',
    'Vicente', 'Reynaldo', 'Denis', 'Orion', 'Jamison',
    'Prince', 'Thiago', 'Duncan', 'Nehemiah', 'Vaughn',
    'Derick', 'Reece', 'Edmond', 'Emil', 'Ace',
    'Legend', 'Ahmad', 'Justice', 'Marlin', 'Aron',
    'Uriel', 'Garland', 'Karson', 'Sonny', 'Gideon',
    'Scotty', 'Knox', 'Matias', 'Cohen', 'Anton',
    'Dion', 'Woodrow', 'Ignacio', 'Efrain', 'Sammie',
    'Nash', 'Phil', 'Marcel', 'Kurtis', 'Jess',
    'Ari', 'Abram', 'Chuck', 'Muhammad', 'Pierre',
    'Ezequiel', 'Luka', 'Braylon', 'Mohamed', 'Keenan',
    'Rusty', 'Zackery', 'Pierce', 'Major', 'Maximilian',
    'Kane', 'Burton', 'Porter', 'Javon', 'Elton',
    'Asa', 'Santos', 'Jarvis', 'Kareem', 'Cleveland',
    'Elvin', 'Ronan', 'Damion', 'Humberto', 'Gunnar',
    'Elvis', 'Isaias', 'Kellen', 'Rickie', 'Iker',
    'Curt', 'Darian', 'Adonis', 'Augustus', 'Arlo',
    'Alvaro', 'Ahmed', 'Nico', 'Moshe', 'Rashad',
    'Aldo', 'Nasir', 'Josh', 'Tyrell', 'Loyd',
    'Bart', 'Deshawn', 'Murray', 'Jamar', 'Mohammad',
    'Carey', 'Denver', 'Grover', 'Colten', 'Cullen',
    'Ulysses', 'Brayan', 'Kolton', 'Galen', 'Ed',
    'Ernie', 'Donte', 'Adolfo', 'Kieran', 'Norbert',
    'Jeffry', 'Ibrahim', 'Coleman', 'Agustin', 'Brice',
    'Erwin', 'Royal', 'Denny', 'Quintin', 'Monty',
    'Lawson', 'Deon', 'Mohammed', 'Brenton', 'Alden',
    'Atticus', 'Hank', 'Houston', 'Atlas', 'Al',
    'Bryon', 'Camron', 'Markus', 'Hal', 'Ronny',
    'Emory', 'Joesph', 'Tyree', 'Kris', 'Gerry',
    'Coy', 'Luciano', 'Dayton', 'Kory', 'Bruno',
    'Kyrie', 'Osvaldo', 'Beckham', 'Trevon', 'Donnell',
    'Braydon', 'Jensen', 'Hayes', 'Carlo', 'Hans',
    'Roscoe', 'Elwood', 'Scot', 'Alphonso', 'Kash',
    'Jamari', 'Norris', 'Killian', 'Gus', 'Jordon',
    'Gianni', 'Kirby', 'Ned', 'Braeden', 'Izaiah',
    'Devan', 'Wiley', 'Benito', 'Eddy', 'Demarcus',
    'Fletcher', 'Milan', 'Kason', 'Armani', 'Jarred',
    'Harris', 'Chadwick', 'Layne', 'Davon', 'Garret',
    'Brycen', 'Malakai', 'Augustine', 'Johan', 'Domingo',
    'Bo', 'Charley', 'Donny', 'Truman', 'Trace',
    'Johnie', 'Russel', 'Davion', 'Mitchel', 'Forest',
    'Julien', 'Daxton', 'Kermit', 'Antwan', 'Sullivan',
    'Thurman', 'Hollis', 'Gino', 'Merlin', 'Irwin',
    'Jayceon', 'Alijah', 'Vito', 'Vince', 'Nigel',
    'Armand', 'Sanford', 'Braylen', 'Deangelo', 'Ryland',
    'Reggie', 'Talon', 'Mathias', 'Omari', 'Jarod',
    'Mekhi', 'Rhys', 'Emmitt', 'Frederic', 'Niko',
    'Tevin', 'Kayson', 'Yahir', 'Odell', 'Cristopher',
    'Devonte', 'Triston', 'Benson', 'Judson', 'Barney',
    'Erich', 'Matthias', 'Korey', 'Carmelo', 'Wilmer',
    'Weldon', 'Kamden', 'Ulises', 'Alonso', 'Mikel',
    'Carmine', 'Rohan', 'Rigoberto', 'Finnegan', 'Ward',
    'Monroe', 'Landyn', 'Kolby', 'Kian', 'Jamel',
    'Delmar', 'Jaron', 'Hassan', 'Marcelo', 'Theron',
    'Odin', 'Santino', 'Shelton', 'Samson', 'Denzel',
    'Maynard', 'Lucian', 'Octavio', 'Dirk', 'Kenton',
    'Chaim', 'Cornell', 'Zayne', 'Linwood', 'Bodhi',
    'Jairo', 'Jacoby', 'Daren', 'Shayne'
]

female_names = [
    'Mary', 'Patricia', 'Jennifer', 'Linda', 'Elizabeth',
    'Barbara', 'Susan', 'Jessica', 'Sarah', 'Karen',
    'Lisa', 'Nancy', 'Betty', 'Sandra', 'Margaret',
    'Ashley', 'Kimberly', 'Emily', 'Donna', 'Michelle',
    'Carol', 'Amanda', 'Melissa', 'Deborah', 'Stephanie',
    'Dorothy', 'Rebecca', 'Sharon', 'Laura', 'Cynthia',
    'Amy', 'Kathleen', 'Angela', 'Shirley', 'Brenda',
    'Emma', 'Anna', 'Pamela', 'Nicole', 'Samantha',
    'Katherine', 'Christine', 'Helen', 'Debra', 'Rachel',
    'Carolyn', 'Janet', 'Maria', 'Catherine', 'Heather',
    'Diane', 'Olivia', 'Julie', 'Joyce', 'Victoria',
    'Ruth', 'Virginia', 'Lauren', 'Kelly', 'Christina',
    'Joan', 'Evelyn', 'Judith', 'Andrea', 'Hannah',
    'Megan', 'Cheryl', 'Jacqueline', 'Martha', 'Madison',
    'Teresa', 'Gloria', 'Sara', 'Janice', 'Ann',
    'Kathryn', 'Abigail', 'Sophia', 'Frances', 'Jean',
    'Alice', 'Judy', 'Isabella', 'Julia', 'Grace',
    'Amber', 'Denise', 'Danielle', 'Marilyn', 'Beverly',
    'Charlotte', 'Natalie', 'Theresa', 'Diana', 'Brittany',
    'Doris', 'Kayla', 'Alexis', 'Lori', 'Marie',
    'Tiffany', 'Kathy', 'Tammy', 'Rose', 'Crystal',
    'Taylor', 'Jane', 'Erin', 'Ava', 'Alyssa',
    'Allison', 'Bonnie', 'Shannon', 'Robin', 'Lillian',
    'Tina', 'Dawn', 'Phyllis', 'Peggy', 'Mia',
    'Paula', 'Audrey', 'Jamie', 'Leslie', 'Valerie',
    'Anne', 'Lois', 'Wendy', 'Connie', 'Wanda',
    'Brianna', 'Vanessa', 'Courtney', 'Cindy', 'Melanie',
    'Jasmine', 'Ella', 'Ruby', 'Tracy', 'Monica',
    'Elaine', 'Norma', 'Rita', 'April', 'Alexandra',
    'Sheila', 'Leah', 'Chloe', 'Erica', 'Sherry',
    'Alicia', 'Michele', 'Ellen', 'Mildred', 'Amelia',
    'Morgan', 'Eleanor', 'Kristen', 'Suzanne', 'Caroline',
    'Katie', 'Annie', 'Irene', 'Joanne', 'Rhonda',
    'Jill', 'Veronica', 'Holly', 'Darlene', 'Carrie',
    'Gail', 'Sylvia', 'Anita', 'Josephine', 'Brooke',
    'Dana', 'Louise', 'Dolores', 'Claire', 'Marjorie',
    'Debbie', 'Sally', 'Eva', 'Renee', 'Savannah',
    'Lynn', 'Kim', 'Kristin', 'Lorraine', 'Jo',
    'Vivian', 'Geraldine', 'Tara', 'Sydney', 'Madeline',
    'Hailey', 'Cathy', 'Cassandra', 'Juanita', 'Molly',
    'Regina', 'Laurie', 'Kaitlyn', 'Eileen', 'Lily',
    'Clara', 'Stacy', 'June', 'Chelsea', 'Sofia',
    'Colleen', 'Esther', 'Lucy', 'Haley', 'Annette',
    'Hazel', 'Lindsey', 'Beth', 'Joann', 'Naomi',
    'Vicki', 'Avery', 'Gina', 'Roberta', 'Lydia',
    'Destiny', 'Carla', 'Kelsey', 'Yvonne', 'Stacey',
    'Shelby', 'Jenna', 'Heidi', 'Terri', 'Rosemary',
    'Loretta', 'Zoe', 'Jeanne', 'Paige', 'Maureen',
    'Faith', 'Jeanette', 'Edith', 'Sabrina', 'Addison',
    'Florence', 'Edna', 'Nora', 'Autumn', 'Gabrielle',
    'Mackenzie', 'Kristina', 'Kaylee', 'Joy', 'Melinda',
    'Deanna', 'Katelyn', 'Carmen', 'Pauline', 'Sue',
    'Charlene', 'Tamara', 'Rosa', 'Alexa', 'Lindsay',
    'Gladys', 'Marlene', 'Gabriella', 'Marcia', 'Lucille',
    'Stella', 'Arlene', 'Riley', 'Aubrey', 'Constance',
    'Erika', 'Thelma', 'Claudia', 'Marissa', 'Tonya',
    'Violet', 'Georgia', 'Brooklyn', 'Kylie', 'Harper',
    'Patsy', 'Tanya', 'Alison', 'Gwendolyn', 'Priscilla',
    'Miranda', 'Daisy', 'Ariana', 'Layla', 'Delores',
    'Marion', 'Caitlin', 'Mariah', 'Maya', 'Ethel',
    'Angelina', 'Jocelyn', 'Isabel', 'Vickie', 'Carole',
    'Nina', 'Yolanda', 'Bernice', 'Glenda', 'Melody',
    'Brandy', 'Ana', 'Makayla', 'Joanna', 'Bailey',
    'Beatrice', 'Zoey', 'Marsha', 'Wilma', 'Sadie',
    'Madelyn', 'Alexandria', 'Camila', 'Brandi', 'Aaliyah',
    'Kara', 'Katrina', 'Marian', 'Bethany', 'Arianna',
    'Toni', 'Penny', 'Sierra', 'Christy', 'Sophie',
    'Jessie', 'Kendra', 'Whitney', 'Natasha', 'Meghan',
    'Briana', 'Dianne', 'Kay', 'Jade', 'Alma',
    'Billie', 'Scarlett', 'Miriam', 'Adriana', 'Gianna',
    'Cora', 'Cecilia', 'Nevaeh', 'Elena', 'Angelica',
    'Penelope', 'Hope', 'Karla', 'Jackie', 'Jenny',
    'Bridget', 'Felicia', 'Elsie', 'Margie', 'Vera',
    'Isabelle', 'Tracey', 'Bertha', 'Becky', 'Summer',
    'Bobbie', 'Ellie', 'Kennedy', 'Lillie', 'Misty',
    'Candace', 'Jacquelyn', 'Shelly', 'Kristine', 'Iris',
    'Maxine', 'Sherri', 'Gabriela', 'Desiree', 'Trinity',
    'Peyton', 'Jillian', 'Genesis', 'Brittney', 'Breanna',
    'Ida', 'Skylar', 'Maggie', 'Rachael', 'Jodi',
    'Sheryl', 'Monique', 'Genevieve', 'Lynda', 'Aria',
    'Natalia', 'Lena', 'Kristi', 'Aurora', 'Bianca',
    'Ariel', 'Meredith', 'Krystal', 'Kelli', 'Rebekah',
    'Krista', 'Bella', 'Shelley', 'Belinda', 'Kate',
    'Gracie', 'Valeria', 'Kristy', 'Serenity', 'Cheyenne',
    'Camille', 'Sandy', 'Mila', 'Candice', 'Elise',
    'Jada', 'Adrienne', 'Rosalie', 'Agnes', 'Liliana',
    'Ramona', 'Mattie', 'Carly', 'Luna', 'Sonia',
    'Sonya', 'Daniela', 'Lola', 'Nichole', 'Kendall',
    'Ivy', 'Jennie', 'Antoinette', 'Juliana', 'Marianne',
    'Mckenzie', 'Guadalupe', 'Robyn', 'Yvette', 'Alana',
    'Rylee', 'Nellie', 'Dora', 'Patty', 'Lynne',
    'Reagan', 'Bessie', 'Leona', 'Pearl', 'Janie',
    'Angie', 'Maryann', 'Sheri', 'Karina', 'Abby',
    'Gayle', 'Mya', 'Rosie', 'Geneva', 'Kari',
    'Jordyn', 'Cassidy', 'Lila', 'Roxanne', 'Celeste',
    'Tabitha', 'Annabelle', 'Payton', 'Kaitlin', 'Viola',
    'Faye', 'Piper', 'Mallory', 'Gertrude', 'Lilly',
    'Alisha', 'Minnie', 'Eliana', 'Dianna', 'Josie',
    'Jody', 'Janelle', 'Mikayla', 'Selena', 'Callie',
    'Harriet', 'Lana', 'Mae', 'Paisley', 'Jan',
    'Jeannette', 'Myra', 'Ada', 'Aimee', 'Vicky',
    'Kiara', 'Emilia', 'Kirsten', 'Allyson', 'Delilah',
    'Tessa', 'Lacey', 'Michaela', 'Caitlyn', 'Alejandra',
    'Adeline', 'Cara', 'Traci', 'Irma', 'Cristina',
    'Velma', 'Susie', 'Eliza', 'Valentina', 'Hayley',
    'Kellie', 'Willow', 'Dominique', 'Gretchen', 'Bernadette',
    'Raquel', 'Marcella', 'Rosemarie', 'Anastasia', 'Jaclyn',
    'Julianna', 'Kylee', 'Esmeralda', 'Eloise', 'Marisa',
    'Lucia', 'Eunice', 'Janis', 'Shelia', 'Giselle',
    'Nadine', 'Ashlyn', 'Aubree', 'Adrianna', 'Marguerite',
    'Betsy', 'Paulette', 'Rochelle', 'Johanna', 'Alaina',
    'Hilda', 'Kelley', 'Khloe', 'Hattie', 'Ginger',
    'Doreen', 'Leilani', 'Jana', 'Latoya', 'Christie',
    'Shawna', 'Myrtle', 'Alexia', 'Aliyah', 'Laurel',
    'Nadia', 'Jasmin', 'Patti', 'Athena', 'Quinn',
    'Elisa', 'Jayla', 'Cecelia', 'Teri', 'Lora',
    'Carolina', 'Serena', 'Brielle', 'Leila', 'Makenzie',
    'Ashlee', 'Jazmin', 'Eden', 'Darla', 'Lynette',
    'Elisabeth', 'Leticia', 'Corinne', 'Raven', 'Mindy',
    'Mercedes', 'Kyla', 'Cassie', 'London', 'Mckenna',
    'Mariana', 'Verna', 'Meagan', 'Delaney', 'Alberta',
    'Mona', 'Kinsley', 'Mabel', 'Isla', 'Shari',
    'Alondra', 'Laila', 'Madeleine', 'Celia', 'Allie',
    'Trisha', 'Tricia', 'Leigh', 'Noelle', 'Dixie',
    'Nikki', 'Reese', 'Mandy', 'Lyla', 'Hadley',
    'Pat', 'Nova', 'Sonja', 'Yesenia', 'Hanna',
    'Alina', 'Stacie', 'Della', 'Ebony', 'Kira',
    'Marla', 'Daphne', 'Clarissa', 'Kristie', 'Alissa',
    'Amaya', 'Olga', 'Kimberley', 'Tami', 'Jazmine',
    'Flora', 'Marina', 'Margarita', 'Kyra', 'Sasha',
    'Lula', 'Kerri', 'Stefanie', 'Lorena', 'Tori',
    'Bonita', 'Fatima', 'Cheri', 'Brooklynn', 'Justine',
    'Jeannie', 'Francine', 'Tasha', 'Tammie', 'Fannie',
    'Sherrie', 'Britney', 'Jolene', 'Tatiana', 'Everly',
    'Ximena', 'Ciara', 'Opal', 'Ronda', 'Emery',
    'Alisa', 'Phoebe', 'Lesley', 'Patrice', 'Inez',
    'Ernestine', 'Katharine', 'Marisol', 'Rachelle', 'Laverne',
    'Tia', 'Therese', 'Janine', 'Erma', 'Kayleigh',
    'Diamond', 'Juliet', 'Charity', 'Pam', 'Sienna',
    'Kasey', 'Kassandra', 'Lucinda', 'Mayra', 'Muriel',
    'Christa', 'Alayna', 'Harmony', 'Tracie', 'Alivia',
    'Deloris', 'Trina', 'Keira', 'Juliette', 'Francesca',
    'Asia', 'Savanna', 'Keri', 'Ryleigh', 'Makenna',
    'Daniella', 'Paris', 'Ashleigh', 'Fiona', 'Lea',
    'Chelsey', 'Mamie', 'Aileen', 'Macy', 'Dina',
    'Talia', 'Shayla', 'Helena', 'Katelynn', 'Janette',
    'Dena', 'Gwen', 'Latasha', 'Jewel', 'Julianne',
    'Myrna', 'Olive', 'Marley', 'Cherie', 'Debora',
    'Haylee', 'Shana', 'Mollie', 'Randi', 'Angelique',
    'Kali', 'Leanne', 'Izabella', 'Antonia', 'Cathleen',
    'Alyson', 'Norah', 'Brenna', 'Ayla', 'Aniyah',
    'Camryn', 'Arielle', 'Hillary', 'Lara', 'Delia',
    'Bette', 'Bettie', 'Malia', 'Elaina', 'Tania',
    'Heaven', 'Joni', 'Adalynn', 'Blanche', 'Karin',
    'Candy', 'Tiana', 'Evangeline', 'Carissa', 'Shanna',
    'Hallie', 'Beulah', 'Emerson', 'Shauna', 'Rena',
    'Adele', 'Presley', 'Raelynn', 'Brynn', 'Cierra',
    'Jayne', 'Sondra', 'Clare', 'Jodie', 'Adalyn',
    'Mable', 'Kailey', 'Melba', 'Teagan', 'Ingrid',
    'Lexi', 'Lou', 'Estelle', 'Lenora', 'Simone',
    'Freda', 'Luz', 'Imani', 'Millie', 'Henrietta',
    'Catalina', 'Estella', 'Eve', 'Reba', 'Kiana',
    'Lorna', 'Jenifer', 'Taryn', 'Staci', 'Greta',
    'Camilla', 'Lizbeth', 'Susanne', 'Elsa', 'Margo',
    'Lorene', 'Julissa', 'Trudy', 'Blanca', 'Kenya',
    'Colette', 'Willa', 'Ashlynn', 'Polly', 'Sage',
    'Viviana', 'Sallie', 'Maribel', 'Aisha', 'Leanna',
    'Londyn', 'Chasity', 'Leann', 'Tatum', 'Alanna',
    'Rosalind', 'Nia', 'Hilary', 'Angeline', 'Jeannine',
    'Bobbi', 'Lia', 'Paola', 'Eula', 'Arya',
    'Jeanine', 'Nyla', 'Bridgette', 'Audra', 'Tiara',
    'Emilee', 'Helene', 'Winifred', 'Deana', 'Arabella',
    'Ericka', 'Raegan', 'Kamryn', 'Larissa', 'Maritza',
    'Lela', 'Tamika', 'Adelaide', 'India', 'Alessandra',
    'Darcy', 'Jeri', 'Emilie', 'Mara', 'Skye',
    'Sheena', 'Angelia', 'Danna', 'Addie', 'Tonia',
    'Keisha', 'Maddison', 'Glenna', 'Lorie', 'Emely',
    'Amara', 'Latonya', 'Cadence', 'Bettye', 'Nayeli',
    'Noemi', 'Marcy', 'Madalyn', 'Lauryn', 'Kaylie',
    'Cali', 'Elliana', 'Rosetta', 'Jami', 'Rylie',
    'Eugenia', 'Madilyn', 'Etta', 'Rosalyn', 'Kiera',
    'Ladonna', 'Aspen', 'Baylee', 'Fay', 'Christi',
    'Yasmin', 'Gemma', 'Sarai', 'Jayda', 'Adelyn',
    'Lilliana', 'Kassidy', 'Imogene', 'Brianne', 'Amie',
    'Susana', 'Dorothea', 'Maeve', 'Perla', 'Maci',
    'Elyse', 'Finley', 'Silvia', 'Macie', 'Kenzie',
    'Karissa', 'Mikaela', 'Katy', 'Ina', 'Terrie',
    'May', 'Samara', 'Gale', 'Maura', 'Kyleigh',
    'Noreen', 'Miracle', 'Essie', 'Lacy', 'Tabatha',
    'Nettie', 'Lyric', 'Bryanna', 'Esperanza', 'Tanisha',
    'Kelsie', 'Gia', 'Ruthie', 'Araceli', 'Amira',
    'Dulce', 'Matilda', 'Lilah', 'Ollie', 'Kiley',
    'Nathalie', 'Precious', 'Rae', 'Ainsley', 'Melisa',
    'Nola', 'Fern', 'Kaylin', 'Itzel', 'Annika',
    'Annmarie', 'Blair', 'Ora', 'Sloane', 'Claudette',
    'Alexus', 'Kinley', 'Chanel', 'Octavia', 'Liana',
    'Valarie', 'Paulina', 'Malinda', 'Latisha', 'Iva',
    'Brynlee', 'Melina', 'Katlyn', 'Haven', 'Margot',
    'Elvira', 'Anya', 'Journey', 'Fernanda', 'Vivienne',
    'Clarice', 'Hollie', 'Nelda', 'Rhoda', 'Lottie',
    'Elva', 'Selina', 'Mavis', 'Saundra', 'Corrine',
    'Carmela', 'Cleo', 'Joselyn', 'Jewell', 'Kimberlee',
    'Janae', 'Elissa', 'Beatriz', 'Abbie', 'Abbey',
    'Ariella', 'Aniya', 'Anahi', 'Susanna', 'Myla',
    'Lorrie', 'Chandra', 'Lilian', 'Elle',
]

class QuizType(Enum):
    ANCESTOR = 1
    DESCENDANT = 2
    COMMON_ANCESTOR = 3
    COMMON_DESCENDANT = 4
    OTHER = 5

answer_templates = [
    (QuizType.ANCESTOR, "{p1_name} is {p2_name}'s ancestor."),
    (QuizType.DESCENDANT, "{p1_name} is {p2_name}'s descendant."),
    (QuizType.COMMON_ANCESTOR, "{p1_name} and {p2_name} share a common ancestor."),
    (QuizType.COMMON_DESCENDANT, "{p1_name} and {p2_name} share a common descendant."),
    (QuizType.OTHER, "None of the above is correct."),
]

def generate_quiz(length, quiz_type, shuffle=False, prompt=DEFAULT_PROMPT):
    character_names = random.sample(male_names + female_names, length)

    match quiz_type:
        case QuizType.ANCESTOR:
            ancestor_relations = [(i, i + 1) for i in range(length - 1)]
        case QuizType.DESCENDANT:
            ancestor_relations = [(i + 1, i) for i in range(length - 1)]
        case QuizType.COMMON_ANCESTOR:
            common_pos = random.randint(1, length - 2)
            ancestor_relations = [(i + 1, i) if i + 1 <= common_pos else (i, i + 1) for i in range(length - 1)]
        case QuizType.COMMON_DESCENDANT:
            common_pos = random.randint(1, length - 2)
            ancestor_relations = [(i, i + 1) if i + 1 <= common_pos else (i + 1, i) for i in range(length - 1)]
        case _:
            raise ValueError("Unsupported quiz type")
    
    if shuffle:
        random.shuffle(ancestor_relations)

    quiz_relations_str = ""
    for p1, p2 in ancestor_relations:
        p1_name = character_names[p1]
        p2_name = character_names[p2]

        if random.choice([True, False]):
            quiz_relations_str += f"* {p1_name} is {p2_name}'s ancestor.\n"
        else:
            quiz_relations_str += f"* {p2_name} is {p1_name}'s descendant.\n"

    p1_name = character_names[0]
    p2_name = character_names[length-1]

    quiz_question_str = f"Determine the lineage relationship between {p1_name} and {p2_name}."
 
    answer_options = answer_templates[:-1]
    if shuffle:
        random.shuffle(answer_options)
    answer_options.append(answer_templates[-1])

    quiz_answers_str = ""
    correct_answer_num = 0
    for i, (quiz_answer_type, quiz_answer_template) in enumerate(answer_options):
        answer_num = i + 1
        quiz_answer = quiz_answer_template.format(p1_name=p1_name, p2_name=p2_name);
        quiz_answers_str += f"{answer_num}. {quiz_answer}\n"
        if quiz_answer_type == quiz_type:
            correct_answer_num = answer_num

    assert(correct_answer_num != 0)

    quiz = prompt.format(quiz_relations=quiz_relations_str.strip(), quiz_question=quiz_question_str.strip(), quiz_answers=quiz_answers_str.strip())
    return quiz, correct_answer_num

def generate_quizzes(length, num_quizzes=10, prompt=DEFAULT_PROMPT, shuffle=False, seed=None):
    if seed is not None:
        random.seed(seed)
    quiz_types = list(QuizType)
    # do not generate QuizType.OTHER quizes
    quiz_types.pop()
    for i in range(num_quizzes):
        for quiz_type in quiz_types:
            quiz, correct_answer = generate_quiz(length, quiz_type, shuffle=shuffle, prompt=prompt)
            yield (str(quiz_type).removeprefix("QuizType."), correct_answer, quiz)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--length", help = "Number of people connected with lineage relationships in the quiz.", type=int, choices=range(4,2049), metavar="[4-2048]", required=True)
    parser.add_argument("-p", "--prompt", help = "Prompt template of the quiz. The default prompt template is: " + repr(DEFAULT_PROMPT), default=DEFAULT_PROMPT)
    parser.add_argument("-s", "--shuffle", help = "Shuffle the order of lineage relations in the quiz.", action="store_true")
    parser.add_argument("-n", "--number", help = "Number of quizzes generated for each valid answer option.", default=10, type=int)
    parser.add_argument("-r", "--seed", help = "Random seed value", default=None, type=int)
    args = parser.parse_args()

    # keep the generated quizzes the same as before for quiz lengths <= 200
    # by truncating the name lists to 100 most popular names
    if args.length <= 200:
        male_names = male_names[0:100]
        female_names = female_names[0:100]

    prompt = codecs.escape_decode(bytes(args.prompt, "utf-8"))[0].decode("utf-8")

    csv_writer = csv.writer(sys.stdout)
    for relation_name, correct_answer, quiz in generate_quizzes(args.length, args.number, prompt, args.shuffle, args.seed):
        csv_writer.writerow([args.length, relation_name, correct_answer, quiz])
 
