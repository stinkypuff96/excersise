import json

easy_questions = [
    {
        "question": 'What is the capital of Germany?',
        "choices": ["1. Munich", "2. Berlin", "3. Frankfurt am Main", "4. Hamburg"],
        "answer": "2"
    },
    {
        "question": "Who was Chancellor of Germany during World War II?",
        "choices": ["1. Angela Merkel", "2. Olaf Schulz", "3. Otto von Bismarck",
                    "4. Adolf Hitler"],
        "answer": "4"
    },
    {
        "question": "Which were the two Major Powers opposing each other during the"
                    " Cold War?",
        "choices": ["1. USA/USSR", "2. Germany/Austria", "3. Italy/Spain",
                    "4. North Africa/ South Africa"],
        "answer": "1"
    },
    {
        "question": "Which individual received most of the blame for the \n"
                    "attack on the World Trade Center on Sept. 11th, 2001?",
        "choices": ["1. Muammar Gaddafi", "2. Muhammad Ali", "3. Osama bin Laden", "4. Sadam Hussein"],
        "answer": "3"
    },
    {
        "question": "Which system did the German philosopher Karl Marx write about for most \n"
                    "of his life?",
        "choices": ["1. Communism", "2. Socialism", "3. Capitalism", "4. Feudalism"],
        "answer": "3"
    },
    {
        "question": "Who invented the iPhone?",
        "choices": ["1. Bill Gates", "2. Tim Apple", "3. Workers at Apple", "4. Steve Jobs"],
            "answer": "3"
    },
    {
        "question": "Which country is the only country in the history of the world to use \n"
                    "an atom bomb?",
        "choices": ["1. Russia", "2. USA", "3. Germany", "4. United Kingdom"],
        "answer": "2"
    },
    {
        "question": "As of 2025, how many years has the U.S. been engaged in a war with \n"
                    "other countries in the world?",
        "choices": ["1. 24", "2. 7", "3. The U.S. has not been at war recently", "4. 12"],
        "answer": "1"
    },
    {
        "question": "Who was the first president of the United States?",
        "choices": ["1. Abraham Lincoln", "2. George Washington", "3. John Adams", "4. Thomas Jefferson"],
        "answer": "2"
    },
    {
        "question": "Which continent is the Sahara Desert located in?",
        "choices": ["1. Asia", "2. Australia", "3. Africa", "4. South America"],
        "answer": "3"
    },
    {
        "question": "In which country did the COVID-19 pandemic first begin?",
        "choices": ["1. USA", "2. China", "3. Italy", "4. India"],
        "answer": "2"
    },
    {
        "question": "Which is the primary language spoken in Brazil?",
        "choices": ["1. Spanish", "2. English", "3. Portuguese", "4. French"],
        "answer": "3"
    },
    {
        "question": "Which war ended with the Treaty of Versailles in 1919?",
        "choices": ["1. World War I", "2. World War II", "3. Vietnam War", "4. Korean War"],
        "answer": "1"
    },
    {
        "question": "Which country built the Great Wall to protect against invasion?",
        "choices": ["1. India", "2. China", "3. Russia", "4. Japan"],
        "answer": "2"
    },
    {
        "question": "Which U.S. president is known for ending slavery?",
        "choices": ["1. George Washington", "4. Theodore Roosevelt", "3. Barack Obama", "4. Abraham Lincoln"],
        "answer": "4"
    },
    {
        "question": "What currency is used in most European Union countries?",
        "choices": ["1. Lev", "2. Euro-dollar", "3. Franc", "4. Euro"],
        "answer": "4"
    }
]

normal_questions = [
    {
        "question": "What year did the Berlin Wall fall?",
        "choices": ["1. 1987", "2. 1989", "3. 1991", "4. 1993"],
        "answer": "2"
    },
    {
        "question": "Who was the first Chancellor of West Germany after World War II?",
        "choices": ["1. Otto von Bismarck", "2. Konrad Adenauer", "3. Helmut Kohl", "4. Willy Brandt"],
        "answer": "2"
    },
    {
        "question": "How many assassination attempts did the U.S. make on Fidel Castro \n"
                    "after the Cuban Revolution?",
        "choices": ["1. Around 10", "2. Around 50", "3. Around 100", "4. Over 600"],
        "answer": "4"
    },
    {
        "question": "What is one major reason the U.S government has supported coups \n"
                    "in Latin America during the 20th century?",
        "choices": ["1. To protect U.S. corporate interests", "2. To support anti-communist regimes",
                    "3. To promote democracy", "4. To prevent terrorism"],
        "answer": "1"
    },
    {
        "question": "Which term is often used to describe the close relationship \n"
                    "between weapons manufacturers and political power in the U.S.?",
        "choices": ["1. Capitalist Core", "2. Economic Hegemony",
                    "3. Military-Industrial Complex", "4. Security Alliance"],
        "answer": "3"
    },
    {
        "question": "Which of the following countries has been under heavy sanctions \n"
                    "by the U.S. despite not posing a direct military threat?",
        "choices": ["1. North Korea", "2. Iran", "3. Venezuela", "4. Russia"],
        "answer": "3"
    },
    {
        "question": "Why did whistleblower Edward Snowden flee the United States in 2013?",
        "choices": ["1. He was evading taxes", "2. He mocked Trump for his small hands",
                    "3. He leaked documents exposing global surveillance by the NSA",
                    "4. He stole military secrets"],
        "answer": "3"
    },
    {
        "question": "Which event is often cited as a false pretext for \nthe U.S. "
                    "invasion of Iraq in 2003?",
        "choices": ["1. Iran's nuclear program", "2. Weapons of Mass Destruction(WMDs)",
                    "3. Saddam Hussein's invasion of Kuwait", "4. The 9/11 attacks"],
        "answer": "2"
    },
    {
        "question": "Which country has the highest number of military \n"
                    "bases outside its own territory?",
        "choices": ["1. China", "2. Russia", "3. France", "4. United States"],
        "answer": "4"
    },
    {
        "question": "Which country has faced widespread international criticism \n"
                    "for its military actions and blockade policies in a \n"
                    "territory, where nearly half the population are children \n"
                    "and living conditions have been described by many as resembling\n"
                    " an open-air prison?",
        "choices": ["1. Israel", "2. Syria", "3. Egypt", "4. Iran"],
        "answer": "1"
    },
    {
        "question": "What was the main reason the United States got involved in the Vietnam War?",
        "choices": ["1. Oil interests", "2. Stop the spread of communism",
                    "3. Retaliation for Pearl Harbor", "4. Trade routes"],
        "answer": "2"
    },
    {
        "question": "Which African country was never colonized by European powers?",
        "choices": ["1. Nigeria", "2. Ethiopia", "3. Ghana", "4. Kenya"],
        "answer": "2"
    },
    {
        "question": "Which civil rights leader was murdered during the Civil Rights Movement?",
        "choices": ["1. Malcolm X", "2. Martin Luther King Jr.", "3. Fred Hampton", "4. All of the above"],
        "answer": "4"
    },
    {
        "question": "The CIA-backed coup in Chile in 1973 overthrew which democratically elected leader?",
        "choices": ["1. Salvador Allende", "2. Hugo Chavez", "3. Che Guevara", "4. Augusto Pinochet"],
        "answer": "1"
    },
    {
        "question": "Which European country colonized India before its independence in 1947?",
        "choices": ["1. France", "2. Spain", "3. Britain", "4. Germany"],
        "answer": "3"
    },
    {
        "question": "After a CIA-backed coup in Chile in 1973, which leader executed over 3000 leftists, \n"
                    "socialists and political critics?",
        "choices": ["1. Salvador Allende", "2. Hugo Chavez", "3. Che Guevara", "Augusto Pinochet"],
        "answer": "4"
    },
    {
        "question": "Which 20th century U.S. war was largely opposed by the American public and led to \n"
                    "widespread protests?",
        "choices": ["1. Korean War", "2. Vietnam War", "3. Iraq War", "4. World War I"],
        "answer": "2"
    },
    {
        "question": "Which event exposed the U.S. government’s surveillance of its own citizens?",
        "choices": ["1. Pentagon Papers", "2. Watergate", "3. Snowden Leaks", "4. WikiLeaks"],
        "answer": "3"
    },
    {
        "question": "Which European country colonized the Congo, leading to one of the most \n"
                    "brutal colonial regimes?",
        "choices": ["1. France", "2. Belgium", "3. Portugal", "4. Germany"],
        "answer": "2"
    },
    {
        "question": "Which U.S. military prison became infamous for torture and human rights \n"
                    "violations during the Iraq War?",
        "choices": ["1. Alcatraz", "2. Abu Ghraib", "3. Rikers Island", "4. Fort Leavenworth"],
        "answer": "2"
    }
]

hard_questions = [
    {
        "question": "Which economic system places profit and private ownership at \n"
                    "the center, often resulting in exploitation of the working class?",
        "choices": ["1. Socialism", "2. Capitalism", "3. Feudalism", "4. Anarchism"],
        "answer": "2"
    },
    {
        "question": "Which global financial institution has been widely \n"
                    "criticized for imposing austerity measures on developing \n"
                    "countries, leading to deep economic hardship for their populations?",
        "choices": ["1. The World Bank", "2. The International Monetary Fund(IMF)",
                    "3. United Nations", "4. World Trade Organization(WTO)"],
        "answer": "2"
    },
    {
        "question": "Which major historical event was largely influenced by \n"
                    "Western powers drawing arbitrary borders, contributing to long-term \n"
                    "conflict and instability in the affected region?",
        "choices": ["1. The Fall of the Berlin Wall", "2. The Marshall Plan",
                    "3. The Formation of the European Union", "4. The Partition of India"],
        "answer": "4"
    },
    {
        "question": "Which modern country is known for providing universal healthcare and \n"
                    "has a higher quality of life for its citizens compared to more developed nations?",
        "choices": ["1. United States", "2. Brazil", "3. Cuba", "4. Australia"],
        "answer": "3"
    },
    {
        "question": "Which concept critiques the rise of corporate power in democratic governments, \n"
                    "arguing that corporate elites hold undue influence over policies that should be \n"
                    "in the interest of the people?",
        "choices": ["1. Plutocracy", "2. Democracy", "3. Oligarchy", "4. Socialism"],
        "answer": "1"
    },
    {
        "question": "According to a 2021 report by Oxfam, how much wealth did the world's 10 richest \n"
                    "men gain during the COVID-19 pandemic?",
        "choices": ["1. $10 billion", "2. $50 billion", "3. $250 billion", "4. $500 billion"],
        "answer": "4"
    },
    {
        "question": "Which one of these global corporations has been accused of exploiting workers \n"
                    "in the Global South by paying low wages and violating labor rights?",
        "choices": ["1. Starbucks", "2. Amazon", "3. Nike", "4. Apple"],
        "answer": "3"
    },
    {
        "question": "Which policy, implemented by the United States and its allies, is often seen \n"
                    "as a form of modern-day imperialism, where military force is used to secure \n"
                    "resources and maintain control over developing nations?",
        "choices": ["1. The Marshall Plan", "2. The Monroe Doctrine", "3. The War on Terror", "4. Colonialism"],
        "answer": "3"
    },
    {
        "question": "Which modern political and economic ideology is primarily concerned with \n"
                    "reducing wealth inequality, promoting social justice, and providing public \n"
                    "goods like healthcare and education?",
        "choices": ["1. Social democracy", "2. Fascism", "3. Neoliberalism", "4. Libertarianism"],
        "answer": "1"
    },
    {
        "question": "Which labor movement of the 19th century played a crucial role in establishing \n"
                    "workers' rights and labor laws in capitalist countries, including the eight-hour workday?",
        "choices": ["1. The Chartist Movement", "2. The Industrial Workers of the World(IWW)", "3. The Labor Unions",
                    "4. The Suffragette Movement"],
        "answer": "2"
    },
    {
        "question": "Which of the following is a major contributor to global carbon emissions, \n"
                    "despite outsourcing much of its production to poorer nations?",
        "choices": ["1. Brazil", "2. India", "3. United States", "4. China"],
        "answer": "3"
    },
    {
        "question": "Which historical movement sought to challenge colonial powers and empower the oppressed peoples in colonized nations by calling for self-determination and independence?",
        "choices": ["1. The Nationalist Movement of the 19th Century", "2. The Non-Aligned Movement",
                    "3. The Civil Rights Movement", "4. The Pan-African Movement"],
        "answer": "4"
    },
    {
        "question": "Which 1977 U.S. operation provided arms and funds to Afghan Mujahideen fighters \n"
                    "(later known as Al Qaeda) during the Cold War?",
        "choices": ["1. Operation Desert Storm", "2. Operation Cyclone", "3. Operation Neptune", "4. Operation Enduring Freedom"],
        "answer": "2"
    },
    {
        "question": "Which 1994 agreement is often criticized for benefiting corporations over workers \n"
                    "and small farmers in North America?",
        "choices": ["1. Paris Agreement", "2. NAFTA", "3. GATT", "4. TPP"],
        "answer": "2"
    },
    {
        "question": "Which economist is known for promoting neoliberal policies such as \n"
                    "deregulation and privatization?",
        "choices": ["1. John Maynard Keynes", "2. Karl Marx", "3. Milton Friedman", "4. Thomas Piketty"],
        "answer": "3"
    },
    {
        "question": "Which company was involved in a major oil spill in the Gulf of Mexico in 2010, \n"
                    "causing massive environmental damage?",
        "choices": ["1. Shell", "2. ExxonMobil", "3. BP", "4. Chevron"],
        "answer": "3"
    },
    {
        "question": "What is the term for a system where corporations exert control over media, \n"
                    "limiting public access to unbiased information?",
        "choices": ["1. Corporate Censorship", "2. Plutocracy", "3. Media Consolidation", "4. News Saturation"],
        "answer": "3"
    },
    {
        "question": "Which infamous private military company was involved in civilian killings in \n"
                    "Iraq and later rebranded itself?",
        "choices": ["1. Halliburton", "2. Blackwater", "3. DynCorp", "4. KBR"],
        "answer": "2"
    },
    {
        "question": "What term is used to describe the practice of using economic policies to \n"
                    "indirectly control and exploit developing countries?",
        "choices": ["1. Colonialism", "2. Neocolonialism", "3. Protectionism", "4. Mercantilism"],
        "answer": "2"
    },
    {
        "question": "Which ideology views global capitalism as a key driver of inequality, environmental \n"
                    "destruction, and imperialism?",
        "choices": ["1. Libertarianism", "2. Marxism", "3. Nationalism", "4. Neorealism"],
        "answer": "2"
    },
    {
        "question": "Which whistleblower released the Iraq and Afghanistan war logs, exposing civilian \n"
                    "casualties and abuses by U.S. forces?",
        "choices": ["1. Edward Snowden", "2. Julian Assange", "3. Daniel Ellsberg", "4. Chelsea Manning"],
        "answer": "4"
    },
    {
        "question": "What was the name of the CIA operation that involved mind control experiments on \n"
                    "unwitting subjects during the Cold War?",
        "choices": ["1. Operation Paperclip", "2. Operation Mockingbird", "3. MK-Ultra", "4. Project Blue Book"],
        "answer": "3"
    },
    {
        "question": "Which U.S. intelligence operation aimed to influence foreign media and academic \n"
                    "institutions during the Cold War, spreading pro-American propaganda?",
        "choices": ["1. Operation Northwoods", "2. Operation Ajax", "3. Operation Mockingbird",
                    "4. Operation Paperclip"],
        "answer": "3"
    },
    {
        "question": "Which country was deliberately overthrown in 1953 through a CIA- and MI6-backed \n"
                    "coup to protect Western oil interests, despite having a democratically \n"
                    "elected leader?",
        "choices": ["1. Egypt", "2. Iran", "3. Chile", "4. Indonesia"],
        "answer": "2"
    }
]

bonus_hard_question = [
    {
        "question": "Which government organization sent anonymous letters to\n"
                          "Martin Luther King Jr. urging him to commit suicide,\n"
                          "shortly before his assassination?",
        "choices": ["1. Central Intelligence Agency(CIA)", "2. Federal Bureau of Investigation(FBI)",
                    "3. National Security Agency(NSA)", "4. Department of Justice(DOJ)"],
        "answer": "2"
    }
]

all_questions = {
    "easy": easy_questions,
    "normal": normal_questions,
    "hard": hard_questions,
    "bonus": bonus_hard_question
}

with open("questions.json", "w", encoding="utf-8") as f:
    json.dump(all_questions, f, indent=4)