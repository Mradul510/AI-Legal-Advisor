"""
Indian Legal Knowledge Base
Contains categorized legal information, IPC sections, Acts, and response templates.
"""

# Legal categories and their descriptions
LEGAL_CATEGORIES = {
    "criminal": "Criminal Law & Indian Penal Code",
    "property": "Property & Real Estate Law",
    "contract": "Contract & Commercial Law",
    "labor": "Labor & Employment Law",
    "family": "Family & Personal Law",
    "consumer": "Consumer Protection Law",
    "cyber": "Cyber & IT Law",
    "constitutional": "Constitutional & Fundamental Rights",
    "tax": "Tax & Financial Law",
    "general": "General Legal Information"
}

# Training data for the classifier
TRAINING_DATA = [
    # Criminal Law
    ("theft robbery stolen crime murder assault", "criminal"),
    ("fir police complaint criminal case arrest bail", "criminal"),
    ("ipc section offense punishment jail sentence", "criminal"),
    ("cheating fraud forgery criminal breach trust", "criminal"),
    ("domestic violence dowry harassment cruelty", "criminal"),
    ("kidnapping abduction wrongful restraint confinement", "criminal"),
    ("defamation insult criminal intimidation", "criminal"),
    ("bailable non-bailable cognizable offense", "criminal"),
    ("anticipatory bail regular bail interim bail", "criminal"),
    ("crpc criminal procedure investigation chargesheet", "criminal"),

    # Property Law
    ("property land house flat apartment ownership", "property"),
    ("registration deed sale purchase transfer title", "property"),
    ("tenant landlord rent lease agreement eviction", "property"),
    ("mutation property tax encumbrance certificate", "property"),
    ("partition ancestral property joint family", "property"),
    ("encroachment trespass illegal possession", "property"),
    ("will succession inheritance property rights", "property"),
    ("rera real estate builder buyer complaint", "property"),
    ("stamp duty registration charges conveyance", "property"),
    ("power of attorney property dispute boundary", "property"),

    # Contract Law
    ("contract agreement terms conditions breach", "contract"),
    ("offer acceptance consideration valid contract", "contract"),
    ("breach contract damages compensation remedy", "contract"),
    ("non-disclosure agreement nda confidentiality", "contract"),
    ("partnership firm llp company formation", "contract"),
    ("service agreement freelance employment contract", "contract"),
    ("indemnity guarantee surety bond", "contract"),
    ("void voidable illegal agreement contract", "contract"),
    ("arbitration mediation dispute resolution", "contract"),
    ("specific performance injunction court order", "contract"),

    # Labor Law
    ("employee employer salary wages payment", "labor"),
    ("termination wrongful dismissal retrenchment layoff", "labor"),
    ("pf provident fund esi gratuity bonus", "labor"),
    ("minimum wages overtime working hours factory", "labor"),
    ("sexual harassment workplace posh prevention", "labor"),
    ("trade union strike lockout industrial dispute", "labor"),
    ("maternity paternity leave benefits entitlement", "labor"),
    ("contract labor outsourcing manpower staffing", "labor"),
    ("notice period resignation full final settlement", "labor"),
    ("workmen compensation accident disability insurance", "labor"),

    # Family Law
    ("marriage divorce separation judicial decree", "family"),
    ("alimony maintenance child custody visitation", "family"),
    ("adoption guardianship minor child welfare", "family"),
    ("dowry prohibition domestic violence protection", "family"),
    ("succession inheritance hindu muslim christian", "family"),
    ("mutual consent contested divorce petition", "family"),
    ("live-in relationship rights cohabitation", "family"),
    ("domestic violence protection order residence", "family"),
    ("child marriage prohibition age consent", "family"),
    ("restitution conjugal rights marital dispute", "family"),

    # Consumer Law
    ("consumer complaint product defect deficiency service", "consumer"),
    ("refund replacement compensation consumer forum", "consumer"),
    ("unfair trade practice misleading advertisement", "consumer"),
    ("ecommerce online shopping delivery return", "consumer"),
    ("insurance claim rejection health life motor", "consumer"),
    ("banking complaint loan emi credit card charges", "consumer"),
    ("medical negligence hospital doctor treatment", "consumer"),
    ("consumer forum district state national commission", "consumer"),
    ("product liability manufacturer seller warranty", "consumer"),
    ("food safety adulteration quality standard fssai", "consumer"),

    # Cyber Law
    ("cyber crime hacking online fraud phishing", "cyber"),
    ("data privacy personal information protection", "cyber"),
    ("social media defamation online harassment trolling", "cyber"),
    ("identity theft impersonation fake profile", "cyber"),
    ("it act information technology section 66", "cyber"),
    ("digital signature electronic record certificate", "cyber"),
    ("cryptocurrency bitcoin regulation rbi", "cyber"),
    ("data breach notification company liability", "cyber"),
    ("online gambling betting regulation legality", "cyber"),
    ("revenge porn morphed images obscene content", "cyber"),

    # Constitutional Law
    ("fundamental rights constitution article freedom", "constitutional"),
    ("right equality discrimination caste religion gender", "constitutional"),
    ("freedom speech expression press censorship", "constitutional"),
    ("right life liberty personal privacy dignity", "constitutional"),
    ("writ petition habeas corpus mandamus certiorari", "constitutional"),
    ("pil public interest litigation supreme high court", "constitutional"),
    ("reservation quota sc st obc category", "constitutional"),
    ("state policy directive principles dpsp", "constitutional"),
    ("amendment constitutional validity judicial review", "constitutional"),
    ("emergency provisions president rule governor", "constitutional"),

    # Tax Law
    ("income tax return filing assessment itr", "tax"),
    ("gst goods services tax invoice credit", "tax"),
    ("tds tcs deduction collection source", "tax"),
    ("capital gains property share investment tax", "tax"),
    ("tax audit penalty interest notice demand", "tax"),
    ("customs duty import export excise", "tax"),
    ("tax exemption deduction section 80c 80d", "tax"),
    ("black money benami transaction penalty", "tax"),
    ("itat appellate tribunal commissioner appeal", "tax"),
    ("advance tax self-assessment tax challan payment", "tax"),
]

# Knowledge base for detailed responses
LEGAL_RESPONSES = {
    "criminal": {
        "overview": "Criminal law in India is primarily governed by the Bharatiya Nyaya Sanhita (BNS) 2023, which replaced the Indian Penal Code (IPC) 1860, along with the Bharatiya Nagarik Suraksha Sanhita (BNSS) 2023 replacing CrPC.",
        "key_acts": [
            "Bharatiya Nyaya Sanhita (BNS) 2023",
            "Bharatiya Nagarik Suraksha Sanhita (BNSS) 2023",
            "Bharatiya Sakshya Adhiniyam (BSA) 2023",
            "Protection of Children from Sexual Offences (POCSO) Act, 2012",
            "Narcotic Drugs and Psychotropic Substances Act, 1985"
        ],
        "tips": [
            "Always file an FIR at the nearest police station for cognizable offenses",
            "You have the right to legal representation from the time of arrest",
            "Bail is the rule, jail is the exception — as per Supreme Court guidelines",
            "Zero FIR can be filed at any police station irrespective of jurisdiction",
            "Anticipatory bail can be sought under Section 482 of BNSS"
        ]
    },
    "property": {
        "overview": "Property law in India covers transfer, ownership, and disputes related to immovable and movable property, governed by the Transfer of Property Act, 1882, Registration Act, 1908, and various state-specific laws.",
        "key_acts": [
            "Transfer of Property Act, 1882",
            "Registration Act, 1908",
            "Indian Stamp Act, 1899",
            "Real Estate (Regulation and Development) Act, 2016 (RERA)",
            "Benami Transactions (Prohibition) Act, 1988"
        ],
        "tips": [
            "Always verify property title through Encumbrance Certificate",
            "Registration is mandatory for property transactions above ₹100",
            "RERA registration is mandatory for all real estate projects",
            "Get a legal opinion before purchasing any property",
            "Mutation of property records is essential after purchase"
        ]
    },
    "contract": {
        "overview": "Contract law in India is governed by the Indian Contract Act, 1872. A valid contract requires free consent, lawful consideration, competent parties, and a lawful object.",
        "key_acts": [
            "Indian Contract Act, 1872",
            "Specific Relief Act, 1963",
            "Arbitration and Conciliation Act, 1996",
            "Limited Liability Partnership Act, 2008",
            "Indian Partnership Act, 1932"
        ],
        "tips": [
            "Always have contracts in writing with clear terms and conditions",
            "Include dispute resolution clauses — arbitration is faster than litigation",
            "Non-compete clauses are generally unenforceable under Indian law",
            "E-contracts and digital signatures are legally valid under IT Act",
            "Limitation period for breach of contract is 3 years"
        ]
    },
    "labor": {
        "overview": "Labor laws in India have been consolidated into 4 Labour Codes: Wages, Social Security, Industrial Relations, and Occupational Safety. These replace 29 older labor laws.",
        "key_acts": [
            "Code on Wages, 2019",
            "Code on Social Security, 2020",
            "Industrial Relations Code, 2020",
            "Occupational Safety, Health and Working Conditions Code, 2020",
            "Sexual Harassment of Women at Workplace Act, 2013 (POSH)"
        ],
        "tips": [
            "Employees are entitled to PF from day one if salary ≤ ₹15,000",
            "Gratuity is payable after 5 years of continuous service",
            "Notice period terms must be clearly mentioned in appointment letter",
            "POSH committee is mandatory for organizations with 10+ employees",
            "Wrongful termination can be challenged under Industrial Disputes Act"
        ]
    },
    "family": {
        "overview": "Family law in India varies based on personal laws — Hindu, Muslim, Christian, and Special Marriage Act. It covers marriage, divorce, maintenance, custody, and succession.",
        "key_acts": [
            "Hindu Marriage Act, 1955",
            "Muslim Personal Law (Shariat) Application Act, 1937",
            "Special Marriage Act, 1954",
            "Protection of Women from Domestic Violence Act, 2005",
            "Hindu Succession Act, 1956"
        ],
        "tips": [
            "Mutual consent divorce requires 6-month cooling period",
            "Wife is entitled to maintenance under Section 125 CrPC",
            "Daughters have equal rights in ancestral property (2005 amendment)",
            "Domestic violence includes emotional, verbal, and economic abuse",
            "Inter-caste and inter-faith marriages are valid under Special Marriage Act"
        ]
    },
    "consumer": {
        "overview": "Consumer protection in India is governed by the Consumer Protection Act, 2019 which provides for a three-tier consumer dispute redressal mechanism.",
        "key_acts": [
            "Consumer Protection Act, 2019",
            "Food Safety and Standards Act, 2006",
            "Bureau of Indian Standards Act, 2016",
            "Legal Metrology Act, 2009",
            "Drugs and Cosmetics Act, 1940"
        ],
        "tips": [
            "Consumer complaints can now be filed online on e-daakhil.nic.in",
            "No lawyer is needed to file a consumer complaint",
            "Claims up to ₹1 crore go to District Commission",
            "Medical negligence cases can be filed under Consumer Protection Act",
            "Product liability now extends to manufacturers, sellers, and service providers"
        ]
    },
    "cyber": {
        "overview": "Cyber law in India is governed by the Information Technology Act, 2000 and its amendments. It covers cyber crimes, data protection, electronic transactions, and digital governance.",
        "key_acts": [
            "Information Technology Act, 2000",
            "IT (Intermediary Guidelines) Rules, 2021",
            "Digital Personal Data Protection Act, 2023",
            "Indian Computer Emergency Response Team (CERT-In) Rules",
            "Bharatiya Nyaya Sanhita provisions on cyber offenses"
        ],
        "tips": [
            "Report cyber crimes at cybercrime.gov.in",
            "Section 66A of IT Act has been struck down — sharing opinions online is not a crime",
            "Take screenshots and preserve digital evidence immediately",
            "Cyber fraud complaints should also be reported to your bank within 3 days",
            "VPN usage is legal in India but not for illegal activities"
        ]
    },
    "constitutional": {
        "overview": "The Constitution of India is the supreme law. It guarantees fundamental rights, establishes the structure of government, and provides for judicial review.",
        "key_acts": [
            "Constitution of India, 1950",
            "Right to Information Act, 2005",
            "Right to Education Act, 2009",
            "Scheduled Castes and Scheduled Tribes (Prevention of Atrocities) Act, 1989",
            "National Human Rights Commission Act, 1993"
        ],
        "tips": [
            "Article 14-18: Right to Equality",
            "Article 19-22: Right to Freedom",
            "Article 23-24: Right against Exploitation",
            "Article 25-28: Right to Freedom of Religion",
            "Article 32: Right to Constitutional Remedies (Heart and soul of Constitution)"
        ]
    },
    "tax": {
        "overview": "Tax law in India comprises Direct Taxes (Income Tax) and Indirect Taxes (GST). The Income Tax Act, 1961 and CGST Act, 2017 are the primary legislations.",
        "key_acts": [
            "Income Tax Act, 1961",
            "Central Goods and Services Tax Act, 2017",
            "Customs Act, 1962",
            "Black Money Act, 2015",
            "Benami Transactions (Prohibition) Act, 1988"
        ],
        "tips": [
            "File ITR even if income is below taxable limit — it's useful for loans and visas",
            "Section 80C allows deduction up to ₹1.5 lakhs",
            "New tax regime is default from AY 2024-25",
            "GST registration is mandatory if turnover exceeds ₹40 lakhs (₹20 lakhs for services)",
            "Advance tax must be paid if tax liability exceeds ₹10,000"
        ]
    },
    "general": {
        "overview": "Indian legal system is based on common law tradition with a written constitution. It has a hierarchical court structure — Supreme Court, High Courts, and District Courts.",
        "key_acts": [
            "Constitution of India",
            "Code of Civil Procedure, 1908",
            "Indian Evidence Act, 1872 (now BSA 2023)",
            "Limitation Act, 1963",
            "Legal Services Authorities Act, 1987"
        ],
        "tips": [
            "Free legal aid is available through NALSA for eligible persons",
            "Lok Adalat provides quick and free dispute resolution",
            "RTI application fee is just ₹10",
            "E-filing of cases is available in most High Courts and Supreme Court",
            "Alternative Dispute Resolution (ADR) is encouraged before litigation"
        ]
    }
}

# Greeting responses
GREETINGS = [
    "Namaste! I'm your AI Legal Advisor specializing in Indian law. How can I help you today?",
    "Hello! Welcome to LAwBOTie. I'm here to help you with legal queries related to Indian law. What's on your mind?",
    "Hi there! I'm your legal AI assistant. Ask me anything about Indian laws, rights, or legal procedures.",
]

# Farewell responses
FAREWELLS = [
    "Thank you for consulting with me. Remember, for critical legal matters, always consult a licensed advocate. Stay legally aware!",
    "Glad I could help! Please consult a practicing lawyer for specific legal action. Take care!",
    "It was a pleasure assisting you. For court representation, please engage a qualified advocate. Goodbye!",
]
