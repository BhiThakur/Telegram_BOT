import os
from typing import Final
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton, BotCommand, InputTextMessageContent
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackContext, CallbackQueryHandler

Token: Final = '6318449750:AAFL3564DVP9L3A5nRYMFH-FsI6eQ5dVIs4'
BOT_USERNAME: Final = 'DevgadCollage_bot'


async def start(update, context):
    user_info = update.message
    print(user_info)
    # Create an inline keyboard with menu buttons
    keyboard = [
        [InlineKeyboardButton("BA", callback_data='menu:BA'),
         InlineKeyboardButton("Bvoc HC", callback_data='menu:BvocHC')
         ],
        [InlineKeyboardButton("Bvoc HT", callback_data='menu:BvocHT'),
         InlineKeyboardButton("BCOM", callback_data='menu:BCOM')
         ],
        [InlineKeyboardButton("BBI", callback_data='menu:BBI'),
         InlineKeyboardButton("BMS", callback_data='menu:BMS')
         ],
        [InlineKeyboardButton("BSC", callback_data='menu:BSC'),
         InlineKeyboardButton("BSC IT", callback_data='menu:BSCIT')
         ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send a message with the inline keyboard
    await update.message.reply_text("Hii 👋👋 \nThis is Question Paper BOT Developed by:\n\nSOUMITRA THAKUR.\n\nChoose Your Faculty 👇", reply_markup=reply_markup)

Standard = ""
Class = ""
Semister = ""
        
# Define the BA function
async def BA(update, context):  
    await context.bot.send_message(
        chat_id=update.callback_query.from_user.id,
        text="Choose your Year:",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [InlineKeyboardButton("First Year", callback_data = 'Year:FY')],
                [InlineKeyboardButton("Second Year", callback_data = 'Year:SY')],
                [InlineKeyboardButton("Third Year", callback_data = 'Year:TY')]
            ]
    )
    )

async def BvocHC(update, context): 
    await context.bot.send_message(
        chat_id=update.callback_query.from_user.id,
        text="Choose your Year:",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [InlineKeyboardButton("First Year", callback_data = 'Year:FY')],
                [InlineKeyboardButton("Second Year", callback_data = 'Year:SY')],
                [InlineKeyboardButton("Third Year", callback_data = 'Year:TY')]
            ]
    )
    )

async def BvocHT(update, context): 
    await context.bot.send_message(
        chat_id=update.callback_query.from_user.id,
        text="Choose your Year:",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [InlineKeyboardButton("First Year", callback_data = 'Year:FY')],
                [InlineKeyboardButton("Second Year", callback_data = 'Year:SY')],
                [InlineKeyboardButton("Third Year", callback_data = 'Year:TY')]
            ]
    )
    )
async def BCOM(update, context): 
    
    await context.bot.send_message(
        chat_id=update.callback_query.from_user.id,
        text="Choose your Year:",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [InlineKeyboardButton("First Year", callback_data = 'Year:FY')],
                [InlineKeyboardButton("Second Year", callback_data = 'Year:SY')],
                [InlineKeyboardButton("Third Year", callback_data = 'Year:TY')]
            ]
    )
    )
async def BBI(update, context): 
    
    await context.bot.send_message(
        chat_id=update.callback_query.from_user.id,
        text="Choose your Year:",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [InlineKeyboardButton("First Year", callback_data = 'Year:FY')],
                [InlineKeyboardButton("Second Year", callback_data = 'Year:SY')],
                [InlineKeyboardButton("Third Year", callback_data = 'Year:TY')]
            ]
    )
    )
async def BMS(update, context): 
    
    await context.bot.send_message(
        chat_id=update.callback_query.from_user.id,
        text="Choose your Year:",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [InlineKeyboardButton("First Year", callback_data = 'Year:FY')],
                [InlineKeyboardButton("Second Year", callback_data = 'Year:SY')],
                [InlineKeyboardButton("Third Year", callback_data = 'Year:TY')]
            ]
    )
    )
async def BSC(update, context): 
    
    await context.bot.send_message(
        chat_id=update.callback_query.from_user.id,
        text="Choose your Year:",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [InlineKeyboardButton("First Year", callback_data = 'Year:FY')],
                [InlineKeyboardButton("Second Year", callback_data = 'Year:SY')],
                [InlineKeyboardButton("Third Year", callback_data = 'Year:TY')]
            ]
    )
    )
async def BSCIT(update, context): 
    
    await context.bot.send_message(
        chat_id=update.callback_query.from_user.id,
        text="Choose your Year:",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [InlineKeyboardButton("First Year", callback_data = 'Year:FY')],
                [InlineKeyboardButton("Second Year", callback_data = 'Year:SY')],
                [InlineKeyboardButton("Third Year", callback_data = 'Year:TY')]
            ]
    )
    )

################################### start Year ###################################
async def FY(update, context): 
    await context.bot.send_message(
        chat_id=update.callback_query.from_user.id,
        text="Choose Semister:",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [InlineKeyboardButton("Semester First", callback_data='Sem:SEM_1')],
                [InlineKeyboardButton("Semester Second", callback_data='Sem:SEM_2')]
            ]
    )
    )

async def SY(update, context): 
    await context.bot.send_message(
        chat_id=update.callback_query.from_user.id,
        text="Choose Semister:",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [InlineKeyboardButton("Semester Third", callback_data='Sem:SEM_3')],
                [InlineKeyboardButton("Semester Forth", callback_data='Sem:SEM_4')]
            ]
    )
    )

async def TY(update, context): 
    await context.bot.send_message(
        chat_id=update.callback_query.from_user.id,
        text="Choose Semister:",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [InlineKeyboardButton("Semester Fifth", callback_data='Sem:SEM_5')],
                [InlineKeyboardButton("Semester Sixth", callback_data='Sem:SEM_6')]
            ]
    )
    )



async def button_clicked(update, context):
    global Standard
    global Class
    global Semister
    # Get the callback data from the button
    callback_data = update.callback_query.data.split(':')
    
    # Check if the callback data is related to the menu
    if callback_data[0] == 'menu':
        Standard = callback_data[1]
        if Standard == 'BA':
            await BA(update, context)
        elif Standard == 'BvocHC':
            await BvocHC(update, context)
        elif Standard == 'BvocHT':
            await BvocHT(update, context)
        elif Standard == 'BCOM':
            await BCOM(update, context)
        elif Standard == 'BBI':
            await BBI(update, context)
        elif Standard == 'BMS':
            await BMS(update, context)
        elif Standard == 'BSC':
            await BSC(update, context)
        elif Standard == 'BSCIT':
            await BSCIT(update, context)
        # else:
        #     # Handle other options if needed
        #     await update.callback_query.edit_message_text(f'You chose {Standard}')
            

    elif callback_data[0] == 'Year':
        Class = callback_data[1]
        if Class == 'FY':
            await FY(update,context)
        elif Class == 'SY':
            await SY(update,context)
        elif Class == 'TY':
            await TY(update,context)
        # else:
        #     # Handle other options if needed
        #     await update.callback_query.edit_message_text(f'You chose {Class}')


    elif callback_data[0] == 'Sem':
        Class = callback_data[1]
        if Class == 'SEM_1':
            await SEM_1(update,context)
        elif Class == 'SEM_2':
            await SEM_2(update,context)
        elif Class == 'SEM_3':
            await SEM_3(update,context)
        elif Class == 'SEM_4':
            await SEM_4(update,context)
        elif Class == 'SEM_5':
            await SEM_5(update,context)
        elif Class == 'SEM_6':
            await SEM_6(update,context)
        # else:
        #     # Handle other options if needed
        #     await update.callback_query.edit_message_text(f'You chose {Class}')


################################### start SEMISTER ###################################

async def SEM_1(update, context):
    # Get the chat ID
    chat_id = update.effective_chat.id

    # Initialize an empty list for pdf_paths
    pdf_paths = []

    # Check the standard and update pdf_paths accordingly
    if Standard == "BA":
        pdf_paths = ['BA/SEM 1/FYBA Foundation course 2023.pdf',
                     'BA/SEM 1/FYBA History 2023.pdf',
                     'BA/SEM 1/FYBA English 2023.pdf',
                     'BA/SEM 1/FYBA Human Geographi 2023.pdf',
                     'BA/SEM 1/FYBA Mararhi Optional 2023.pdf',
                     'BA/SEM 1/FYBA Micro Economics 2023.pdf',
                     'BA/SEM 1/FYBA NCC Studies 2023.pdf',
                     'BA/SEM 1/FYBA Marathi Composory 2023.pdf'
                     ]
        
    elif Standard == "BvocHC":
        pdf_paths = ['BVOC HC/SEM 1/FYBVOC HC English Primary Helthcare & Hygiene.pdf',
                     'BVOC HC/SEM 1/FYBVOC HC English.pdf'
                     ]
        
    elif Standard == "BvocHT":
        pdf_paths = ['BVOC HT/SEM 1/SYBVOC HT ENGLISH.pdf',
                     'BVOC HT/SEM 1/SYBVOC HT GENERAL EDUCATION TOURISM POLICIES & PLANNING.pdf'
                     ]
        
    elif Standard == "BCOM":
        pdf_paths = ['BCOM/SEM 1/FYBCOM Business Communication.pdf',
                     'BCOM/SEM 1/FYBCOM Business Economics Marathi.pdf',
                     'BCOM/SEM 1/FYBCOM Business Economics.pdf',
                     'BCOM/SEM 1/FYBCOM Commerce Marathi.pdf',
                     'BCOM/SEM 1/FYBCOM Commerce.pdf',
                     'BCOM/SEM 1/FYBCOM Environmental Studies Marathi.pdf',
                     'BCOM/SEM 1/FYBCOM Environmental Studies.pdf',
                     'BCOM/SEM 1/FYBCOM Foundation Course Marathi.pdf',
                     'BCOM/SEM 1/FYBCOM Foundation Course.pdf',
                     'BCOM/SEM 1/FYBCOM Mathematical and Statistical Techniques.pdf',
                     'BCOM/SEM 1/FYBCOM NCC Studies.pdf'
                     ]
        
    elif Standard == "BBI":
        pdf_paths = ['BBI/SEM 1/FYBBI  Financial Accounting-I.pdf',
                     'BBI/SEM 1/FYBBI BUSINESS COMMUNICATION-I.pdf',
                     'BBI/SEM 1/FYBBI BUSINESS ECONOMICS -1.pdf',
                     'BBI/SEM 1/FYBBI Environment & Management Or Financial Services.pdf',
                     'BBI/SEM 1/FYBBI FOUNDATION COURSE - I.pdf',
                     'BBI/SEM 1/FYBBI NCC Studies.pdf',
                     'BBI/SEM 1/FYBBI PRINCIPLES OF MANAGEMENT.pdf',
                     'BBI/SEM 1/FYBBI Quantitative Methods I.pdf',
                     ]
        
    elif Standard == "BMS":
        pdf_paths = ['BMS/SEM 1/FYBMS BUSINESS COMMUINCATION-I.pdf',
                     'BMS/SEM 1/FYBMS BUSINESS ECONOMICS-1.pdf',
                     'BMS/SEM 1/FYBMS BUSINESS LAW.pdf',
                     'BMS/SEM 1/FYBMS BUSSINESS STATISTICS.pdf',
                     'BMS/SEM 1/FYBMS FOUNDATION OF HUMAN SKILLS.pdf',
                     'BMS/SEM 1/FYBMS INTRODUCTION TO FINANCIAL ACCOUNTING.pdf',
                     'BMS/SEM 1/FYBMS NCC Studies.pdf',
                     'BMS/SEM 1/FYBMS OUNDATION COURSE - I.pdf'
                     ]
        

    elif Standard == "BSC":
        pdf_paths = ['BSC/SEM 1/FYBSC Botany Paper - II.pdf',
                     'BSC/SEM 1/FYBSC Foundation Course.pdf',
                     'BSC/SEM 1/FYBSC General Chemistry -II.pdf',
                     'BSC/SEM 1/FYBSC General Chemistry I.pdf',
                     'BSC/SEM 1/FYBSC Mathematics Paper I.pdf',
                     'BSC/SEM 1/FYBSC Mathematics Paper II.pdf',
                     'BSC/SEM 1/FYBSC NCC Studies.pdf',
                     'BSC/SEM 1/FYBSC PLANT DIVERSITY I.pdf',
                     'BSC/SEM 1/FYBSC USPH 101.pdf',
                     'BSC/SEM 1/FYBSC USPH 102.pdf',
                     'BSC/SEM 1/FYBSC Z0OLOGY PAPER-I.pdf',
                     'BSC/SEM 1/FYBSC Z0OLOGY PAPER-I.pdf'
                     ]
        
    elif Standard == "BSCIT":
        pdf_paths = ['BSC IT/SEM 1/FY IT  DATABASE MANGEMET SYSTEM.pdf',
                     'BSC IT/SEM 1/FY IT Communication Skill.pdf',
                     'BSC IT/SEM 1/FY IT Computational Logic and Discrete Structure.pdf',
                     'BSC IT/SEM 1/FY IT Digital Electronics.pdf',
                     'BSC IT/SEM 1/FY IT ProgrammingWith C.pdf',
                     ]

    # Send the initial message only once
    await context.bot.send_message(chat_id=chat_id, text="Question papers 2023-24")

    # Send the PDF files to the user
    delay_seconds = 10
    write_timeout=35
    read_timeout=20 
    for pdf_path in pdf_paths:
        with open(pdf_path, 'rb') as file:
            await context.bot.send_document(chat_id=chat_id, document=file)



############################# ############################# #############################
############################# SEM 2 ###################################               

async def SEM_2(update, context):
    # Get the chat ID
    chat_id = update.effective_chat.id

    # Initialize an empty list for pdf_paths
    pdf_paths = []

    # Check the standard and update pdf_paths accordingly
    if Standard == "BA":
        pdf_paths = ['BA/SEM 2/Communication Skills In English 2022-23.pdf',
                     'BA/SEM 2/English 2022-23.pdf',
                     'BA/SEM 2/Foundation Course 2022-23.pdf',
                     'BA/SEM 2/Geography Of Enviroment.pdf',
                     'BA/SEM 2/Marathi 2022-23.pdf',
                     'BA/SEM 2/History I 2022-23.pdf',
                     'BA/SEM 2/Marathi(ANC)2022-23.pdf',
                     'BA/SEM 2/Micro Economics 2022-23.pdf',
                     'BA/SEM 2/NCC Studies 2022-23.pdf',
                     'BA/SEM 2/UARD 2022-23.pdf'
                     ]
    elif Standard == "BvocHC":
        pdf_paths = ['BVOC HC/SEM 2/FYBVOC HC ANATOMY OF HUMAIY BODY - LIFE PROCESS I.pdf',
                     'BVOC HC/SEM 2/FYBVOC HC BEHAVTORAL SCIENCE PSYCHOLOGY AND SOCIOLOGY.pdf'
                     ]
        
    elif Standard == "BvocHT":
        pdf_paths = ['BVOC HT/SEM 2/FYBVOC HT Ganeral Education Etraprenurship and Tourism.pdf',
                     'BVOC HT/SEM 2/FYBVOC HT Ganral Education & Tour Opration Management.pdf',
                     ]
        
    elif Standard == "BCOM":
        pdf_paths = ['BCOM/SEM 2/FYBCOM Accountancy and Financial Management.pdf',
                     'BCOM/SEM 2/FYBCOM BUSINESS COMMUNICATI0N.pdf',
                     'BCOM/SEM 2/FYBCOM Business Economics Marathi.pdf',
                     'BCOM/SEM 2/FYBCOM Business Economics.pdf',
                     'BCOM/SEM 2/FYBCOM Commerce Marathi.pdf',
                     'BCOM/SEM 2/FYBCOM Commerce.pdf',
                     'BCOM/SEM 2/FYBCOM ENYIRONMENTAL STUDIES.pdf',
                     'BCOM/SEM 2/FYBCOM Foundation Course Marathi.pdf',
                     'BCOM/SEM 2/FYBCOM Foundation Course.pdf',
                     'BCOM/SEM 2/FYBCOM Mathematical and Statistical Techniques-l.pdf',
                     'BCOM/SEM 2/FYBCOM NCC Studies.pdf'
                     ]
        
    elif Standard == "BBI":
        pdf_paths = ['BBI/SEM 2/FYBBI BUSINESS COMMLTNICATION-II.pdf',
                     'BBI/SEM 2/FYBBI BUSINESS LAW.pdf',
                     'BBI/SEM 2/FYBBI FINANCIAL ACCOUNTING-II.pdf',
                     'BBI/SEM 2/FYBBI FOUNDATION COIIRSE - II.pdf',
                     'BBI/SEM 2/FYBBI NCC Studies.pdf',
                     'BBI/SEM 2/FYBBI ORGANIZATIONAL BEHAVIOR.pdf',
                     'BBI/SEM 2/FYBBI PRINCIPLES & PRACTICES OF BANKING & INSURANCE.pdf',
                     'BBI/SEM 2/FYBBI Quantitative Methods-II.pdf'
                     ]
        
    elif Standard == "BMS":
        pdf_paths = ['BMS/SEM 2/FYBMS BUSINESS COMMUNICATION II.pdf',
                     'BMS/SEM 2/FYBMS BUSINESS ENVIOROMENT.pdf',
                     'BMS/SEM 2/FYBMS BUSSINESS MATTTEMATICS.pdf',
                     'BMS/SEM 2/FYBMS Foundation Course ll.pdf',
                     'BMS/SEM 2/FYBMS INDUSTRIAL LAW.pdf',
                     'BMS/SEM 2/FYBMS NCC Studies.pdf',
                     'BMS/SEM 2/FYBMS PRINCIPLES OF MANAGMENT.pdf',
                     'BMS/SEM 2/FYBMS PRINCIPLES OF MARKETING.pdf'
                     ]
        
    elif Standard == "BSC":
        pdf_paths = ['BSC/SEM 2/FYBSC Botany Paper - II.pdf',
                     'BSC/SEM 2/FYBSC Botany Paper - l.pdf',
                     'BSC/SEM 2/FYBSC Foundation course Marathi.pdf',
                     'BSC/SEM 2/FYBSC Foundation course.pdf',
                     'BSC/SEM 2/FYBSC General Chemi.pdf',
                     'BSC/SEM 2/FYBSC General Chemistry.pdf',
                     'BSC/SEM 2/FYBSC Mathematics Paper-l.pdf',
                     'BSC/SEM 2/FYBSC Mathematics Paper-lI.pdf',
                     'BSC/SEM 2/FYBSC NCC Studies.pdf',
                     'BSC/SEM 2/FYBSC USPH 201.pdf',
                     'BSC/SEM 2/FYBSC USPH 202.pdf',
                     'BSC/SEM 2/FYBSC ZOOLOGY PAPER-l.pdf',
                     'BSC/SEM 2/FYBSC ZOOLOGY PAPER-lI.pdf'
                     ]
        
    elif Standard == "BSCIT":
        pdf_paths = ['BSC IT/SEM 2/FYIT Green Computing.pdf',
                     'BSC IT/SEM 2/FYIT Microprocessor Architecture.pdf',
                     'BSC IT/SEM 2/FYIT Numerical Method.pdf',
                     'BSC IT/SEM 2/FYIT OBJOCT ORIENTED PROGRAMMING WITH C++.pdf',
                     'BSC IT/SEM 2/FYIT Web Applications development.pdf'
                     ]        

    # Send the initial message only once
    await context.bot.send_message(chat_id=chat_id, text="Question papers 2023-24")

    # Send the PDF file to the user
    delay_seconds = 10
    write_timeout=35
    read_timeout=20 
    for pdf_path in pdf_paths:
        with open(pdf_path, 'rb') as file:
            await context.bot.send_document(chat_id=chat_id, document=file)




async def SEM_3(update, context):
    # Get the chat ID
    chat_id = update.effective_chat.id

    # Initialize an empty list for pdf_paths
    pdf_paths = []
    if Standard == "BA":
        pdf_paths = ['BA/SEM 3/SYBA  2023 Travel and Torism.pdf',
                     'BA/SEM 3/SYBA 2023 Bhasha & Boli Abhyas.pdf',
                     'BA/SEM 3/SYBA 2023 English Optional.pdf',
                     'BA/SEM 3/SYBA 2023 Foundation course.pdf',
                     'BA/SEM 3/SYBA 2023 Geography III.pdf',
                     'BA/SEM 3/SYBA 2023 Geography of Maharashtra.pdf',
                     'BA/SEM 3/SYBA 2023 History II.pdf',
                     'BA/SEM 3/SYBA 2023 Kathan Sahitya.pdf',
                     'BA/SEM 3/SYBA 2023 Micro Economics II.pdf',
                     'BA/SEM 3/SYBA 2023 NCC Studies.pdf',
                     'BA/SEM 3/SYBA 2023 Public finance III.pdf',
                     'BA/SEM 3/SYBA 2023 UARD  301.pdf',
                     'BA/SEM 3/SYBA 2023 UARD 302.pdf',
                     ]
    elif Standard == "BvocHC":
        pdf_paths = ['BVOC HC/SEM 3/SYBVOC HC ANATOMY OF HUMAN BODY- LIFE PROCESSES - I.pdf',
                     'BVOC HC/SEM 3/SYBVOC HC Child Health Care Nursing.pdf',
                     'BVOC HC/SEM 3/SYBVOC HC NURSING FOUNDATION.pdf'
                     ]
        
    elif Standard == "BvocHT":
        pdf_paths = ['BVOC HT/SEM 3/SYBVOC HT BUSINESS COMMUNICATION.pdf',
                     'BVOC HT/SEM 3/SYBVOC HT GE CUSTOMER RELATIONSHIP MANAGEMENT.pdf',
                     'BVOC HT/SEM 3/SYBVOC HT GENERAL EDUCATION TOURISM MARKETING & MANAGEMENT.pdf',
                     ]
        
    elif Standard == "BCOM":
        pdf_paths = ['BCOM/SEM 3/SYBCOM ACC and FIN Mangement III.pdf',
                     'BCOM/SEM 3/SYBCOM Advertising I Marathi.pdf',
                     'BCOM/SEM 3/SYBCOM Advertising I.pdf',
                     'BCOM/SEM 3/SYBCOM Bus. Economics II.pdf',
                     'BCOM/SEM 3/SYBCOM Bus. Law I Marathi.pdf',
                     'BCOM/SEM 3/SYBCOM Bus. Law I.pdf',
                     'BCOM/SEM 3/SYBCOM Commerce III Marathi.pdf',
                     'BCOM/SEM 3/SYBCOM Commerce III.pdf',
                     'BCOM/SEM 3/SYBCOM Foundation Course II.pdf',
                     'BCOM/SEM 3/SYBCOM Introduction to Mangement Accounting.pdf',
                     'BCOM/SEM 3/SYBCOM NCC Studies.pdf'
                     ]
        
    elif Standard == "BBI":
        pdf_paths = ['BBI/SEM 3/SYBBI  Financial Management - I.pdf',
                     'BBI/SEM 3/SYBBI Direct Taxation.pdf',
                     'BBI/SEM 3/SYBBI Financial Markets.pdf',
                     'BBI/SEM 3/SYBBI Foundation Course III.pdf',
                     'BBI/SEM 3/SYBBI Information Technology I.pdf',
                     'BBI/SEM 3/SYBBI MANAGEMENT ACCOUNTING.pdf',
                     'BBI/SEM 3/SYBBI NCC Stuides.pdf'
                     ]
        
    elif Standard == "BMS":
        pdf_paths = ['BMS/SEM 3/SYBMS ACCOUNTING FOR MANAGERIAL DECISION.pdf',
                     'BMS/SEM 3/SYBMS Basics of Financial Services.pdf',
                     'BMS/SEM 3/SYBMS BUSINESS PLANNING AND ENT. MANAGEMENT.pdf',
                     'BMS/SEM 3/SYBMS Foundation Course III.pdf',
                     'BMS/SEM 3/SYBMS Information Technology 1.pdf',
                     'BMS/SEM 3/SYBMS INTRODUCTION TO COST ACCOUNTING.pdf',
                     'BMS/SEM 3/SYBMS NCC Studies.pdf',
                     'BMS/SEM 3/SYBMS Strategic Management.pdf'
                     ]
        
    elif Standard == "BSC":
        pdf_paths = ['BSC/SEM 3/SYBSC  FORM AND FUNCTION I.pdf',
                     'BSC/SEM 3/SYBSC Analytical Chemistry.pdf',
                     'BSC/SEM 3/SYBSC CURRENT TRENDS IN PLANT SCIENCES I.pdf',
                     'BSC/SEM 3/SYBSC FOUNDATION COURSE- II.pdf',
                     'BSC/SEM 3/SYBSC General Chemistry I.pdf',
                     'BSC/SEM 3/SYBSC General Chemistry II.pdf',
                     'BSC/SEM 3/SYBSC Mathematics Paper I.pdf',
                     'BSC/SEM 3/SYBSC Mathematics Paper II.pdf',
                     'BSC/SEM 3/SYBSC Mathematics Paper III.pdf',
                     'BSC/SEM 3/SYBSC NCC Studies.pdf',
                     'BSC/SEM 3/SYBSC PLANT DIVERSITY II.pdf',
                     'BSC/SEM 3/SYBSC Thermodynamics and temp. transducers.pdf',
                     'BSC/SEM 3/SYBSC USPH302.pdf',
                     'BSC/SEM 3/SYBSC USPH303.pdf'
                     ]
        
    elif Standard == "BSCIT":
        pdf_paths = ['BSC IT/SEM 3/SYBSC IT Applied Mathematics.pdf',
                     'BSC IT/SEM 3/SYBSC IT Computer Network.pdf',
                     'BSC IT/SEM 3/SYBSC IT Data Structures.pdf',
                     'BSC IT/SEM 3/SYBSC IT Operating systems.pdf',
                     'BSC IT/SEM 3/SYBSC IT Python Programming.pdf'
                     ] 

    # Send the initial message only once
    await context.bot.send_message(chat_id=chat_id, text="Question papers 2023-24")

    # Send the PDF file to the user
    delay_seconds = 10
    write_timeout=35
    read_timeout=20 
    for pdf_path in pdf_paths:
            with open(pdf_path, 'rb') as file:
                await context.bot.send_document(chat_id=chat_id, document=file)

async def SEM_4(update, context):
    # Get the chat ID
    chat_id = update.effective_chat.id

    # Initialize an empty list for pdf_paths
    pdf_paths = []
    if Standard == "BA":
        pdf_paths = ['BA/SEM 4/SYBA 2022-23 English Optional II.pdf',
                     'BA/SEM 4/SYBA 2022-23 Foundation course.pdf',
                     'BA/SEM 4/SYBA 2022-23 Geography II.pdf',
                     'BA/SEM 4/SYBA 2022-23 Geography III.pdf',
                     'BA/SEM 4/SYBA 2022-23 History II.pdf',
                     'BA/SEM 4/SYBA 2022-23 History III.pdf',
                     'BA/SEM 4/SYBA 2022-23 Indian Economics III.pdf',
                     'BA/SEM 4/SYBA 2022-23 Introductio to Poetry.pdf',
                     'BA/SEM 4/SYBA 2022-23 Marathi II.pdf',
                     'BA/SEM 4/SYBA 2022-23 Marathi III.pdf',
                     'BA/SEM 4/SYBA 2022-23 Micro Economics II.pdf',
                     'BA/SEM 4/SYBA 2022-23 RD III.pdf',
                     'BA/SEM 4/SYBA 2022-23 Travel Tourism.pdf',
                     'BA/SEM 4/SYBA 2022-23 UARD 402.pdf'
                     ]
        
    elif Standard == "BvocHC":
        pdf_paths = ['BVOC HC/SEM 4/SYBVOC HC CLTNICAL PHARMACOLOCY AND MICROBIOLOGY.pdf',
                     'BVOC HC/SEM 4/SYBVOC HC GENERAL EDUCATION E-COMMERCE & TOURISM TEGISLATION.pdf'
                     ]
        
    elif Standard == "BvocHT":
        await context.bot.send_message(chat_id=chat_id, text="Sorry, we don't have Semester Four PDFs available right now.")

    elif Standard == "BCOM":
        pdf_paths = ['BCOM/SEM 4/SYBCOM  ACC & FIN  MNGT IV.pdf',
                     'BCOM/SEM 4/SYBCOM  BUSINESS LAW - II Marathi.pdf',
                     'BCOM/SEM 4/SYBCOM  BUSINESS LAW - II.pdf',
                     'BCOM/SEM 4/SYBCOM Advertising -II Marathi.pdf',
                     'BCOM/SEM 4/SYBCOM Advertising -II.pdf',
                     'BCOM/SEM 4/SYBCOM Auditing Marathi.pdf',
                     'BCOM/SEM 4/SYBCOM Auditing.pdf',
                     'BCOM/SEM 4/SYBCOM Business Economics - II Marathi.pdf',
                     'BCOM/SEM 4/SYBCOM Business Economics - II.pdf',
                     'BCOM/SEM 4/SYBCOM Commerce IV Marathi.pdf',
                     'BCOM/SEM 4/SYBCOM Commerce IV.pdf',
                     'BCOM/SEM 4/SYBCOM FOUNDATION COURSE-II Marathi.pdf',
                     'BCOM/SEM 4/SYBCOM FOUNDATION COURSE-II.pdf'
                     ]
        
    elif Standard == "BBI":
        pdf_paths = ['BBI/SEM 4/SYBBI AN OVERVIEW OF INSURANCE SECTOR.pdf',
                     'BBI/SEM 4/SYBBI BUSINESS ECONON{ICS - II.pdf',
                     'BBI/SEM 4/SYBBI COUISTOMER RELATIONSHIP MANAGEMENT.pdf',
                     'BBI/SEM 4/SYBBI COST ACCOUNTING.pdf',
                     'BBI/SEM 4/SYBBI FINANCIAL MANAGEMENT  II.pdf',
                     'BBI/SEM 4/SYBBI Information Technology I.pdf',
                     'BBI/SEM 4/SYBBI SCORPORATE & SECURITY LAW.pdf'
                     ]
        
    elif Standard == "BMS":
        pdf_paths = ['BMS/SEM 4/SYBMS  Financial Institutions and Marke.pdf',
                     'BMS/SEM 4/SYBMS  Information Technology I.pdf',
                     'BMS/SEM 4/SYBMS BUSINESS ECONOMICS - II.pdf',
                     'BMS/SEM 4/SYBMS BUSINESS REASEARCH METHODS.pdf',
                     'BMS/SEM 4/SYBMS Foundation Course.pdf',
                     'BMS/SEM 4/SYBMS PRODUCNON & TOTAT QUANTITY MANAGEMENT.pdf',
                     'BMS/SEM 4/SYBMS STRATEGIC COST MANAGEMENT.pdf'
                     ]
        
    elif Standard == "BSC":
        pdf_paths = ['BSC/SEM 4/SYBSC Auatrfiical Chemistry.pdf',
                     'BSC/SEM 4/SYBSC Botany Paper I.pdf',
                     'BSC/SEM 4/SYBSC Botany Paper II.pdf',
                     'BSC/SEM 4/SYBSC Botany Paper III.pdf',
                     'BSC/SEM 4/SYBSC Foundation Cours II.pdf',
                     'BSC/SEM 4/SYBSC General Chemistry II.pdf',
                     'BSC/SEM 4/SYBSC General Chemistry.pdf',
                     'BSC/SEM 4/SYBSC Mathematics Paper- I.pdf',
                     'BSC/SEM 4/SYBSC Mathematics Paper-II.pdf',
                     'BSC/SEM 4/SYBSC Mathematics Paper-III.pdf',
                     'BSC/SEM 4/SYBSC Physics III.pdf',
                     'BSC/SEM 4/SYBSC USPH 401.pdf',
                     'BSC/SEM 4/SYBSC USPH 402.pdf'
                     ]
        
    elif Standard == "BSCIT":
        pdf_paths = ['BSC IT/SEM 4/SYIT ComPuter GraPhics.pdf',
                     'BSC IT/SEM 4/SYIT Computer Oriented Statistical Methods.pdf',
                     'BSC IT/SEM 4/SYIT Core Java.pdf',
                     'BSC IT/SEM 4/SYIT Embedded System.pdf',
                     'BSC IT/SEM 4/SYIT Software Enginee.pdf'
                     ]

    # Send the initial message only once
    await context.bot.send_message(chat_id=chat_id, text="Question papers 2023-24")

    # Send the PDF file to the user
    delay_seconds = 10
    write_timeout=35
    read_timeout=20    
    for pdf_path in pdf_paths:
            with open(pdf_path, 'rb') as file:
                await context.bot.send_document(chat_id=chat_id, document=file)


async def SEM_5(update, context):
    # Get the chat ID
    chat_id = update.effective_chat.id

    # Initialize an empty list for pdf_paths
    pdf_paths = []
    if Standard == "BA":
        # Send the initial message only once
        await context.bot.send_message(chat_id=chat_id, text="Question papers 2023-24")

        await context.bot.send_message(chat_id=chat_id, text="Six Economics 👇")
        pdf_paths = ['BA/SEM 5/ECONOMICS/TYBA ECONOMICS  - ADVENCED MICRO ECONOMICS III.pdf',
                     'BA/SEM 5/ECONOMICS/TYBA ECONOMICS  - ECONOMICS OF AGRICULTURE _ CO OPERATION.pdf',
                     'BA/SEM 5/ECONOMICS/TYBA ECONOMICS  - ECONOMICS OF GROWTH AND DEVELOPMENT.pdf',
                     'BA/SEM 5/ECONOMICS/TYBA ECONOMICS  - RESEARCH METHODOLOGY.pdf',
                     'BA/SEM 5/ECONOMICS/TYBA ECONOMICS - HISTORY OF ECONOMIC THOUGHT.pdf',
                     'BA/SEM 5/ECONOMICS/TYBA ECONOMICS- ENVIRONMENTAL ECONOMICS.pdf'
                    ]
        delay_seconds = 10
        write_timeout=35
        read_timeout=20
        for pdf_path in pdf_paths:
                with open(pdf_path, 'rb') as file:
                    await context.bot.send_document(chat_id=chat_id, document=file)

        await context.bot.send_message(chat_id=chat_id, text="Six English 👇")
        pdf_paths = ['BA/SEM 5/ENGLISH/TYBA ENGLISH  SEM V NOV 2022 - DRAMA _ THEATURE I.pdf',
                     'BA/SEM 5/ENGLISH/TYBA ENGLISH SEM V NOV 2022 - 16TH TO 18 CENTURY ENGLISH LITERATURE.pdf',
                     'BA/SEM 5/ENGLISH/TYBA ENGLISH SEM V NOV 2022 - 19TH CENTURY ENGLISH LITRATURE.pdf',
                     'BA/SEM 5/ENGLISH/TYBA ENGLISH SEM V NOV 2022 - 20TH CENTURY BRITISH LITERATURE.pdf',
                     'BA/SEM 5/ENGLISH/TYBA ENGLISH SEM V NOV 2022 - GRAMMER AND ART OF WRITING.pdf',
                     'BA/SEM 5/ENGLISH/TYBA ENGLISH SEM V NOV 2022 - LITERARY CRITICISM.pdf'
                    ]

        # Send the PDF file to the user
        delay_seconds = 10
        write_timeout=35
        read_timeout=20
        for pdf_path in pdf_paths:
                with open(pdf_path, 'rb') as file:
                    await context.bot.send_document(chat_id=chat_id, document=file)


        await context.bot.send_message(chat_id=chat_id, text="Six Geography 👇")
        pdf_paths = ['BA/SEM 5/GEOGRAPHY/TYBA GEOGRAPHY  SEM V NOV 2022 - GEOGRAPHY OF RESOURCES.pdf',
                     'BA/SEM 5/GEOGRAPHY/TYBA GEOGRAPHY SEM V  NOV 2022 - GEOGRAPHY OF MAHARASHTRA.pdf',
                     'BA/SEM 5/GEOGRAPHY/TYBA GEOGRAPHY SEM V NOV 2022 - GEOGRAPHY OF SETTLEMENT.pdf',
                     'BA/SEM 5/GEOGRAPHY/TYBA GEOGRAPHY SEM V NOV 2022 - REGIONAL PLANNING AND DEVELOPMENT.pdf'   
                    ]

        # Send the PDF file to the user
        delay_seconds = 10
        write_timeout=35
        read_timeout=20
        for pdf_path in pdf_paths:
                with open(pdf_path, 'rb') as file:
                    await context.bot.send_document(chat_id=chat_id, document=file)

        await context.bot.send_message(chat_id=chat_id, text="Six History 👇")
        pdf_paths = ['BA/SEM 5/HISTORY/TYBA HISTORY SEM V NOV 2022 -  INTRODUCTION TO ARCHAEOLOGY.pdf',
                     'BA/SEM 5/HISTORY/TYBA HISTORY SEM V NOV 2022 - HISTORY OF CONTEMPORARY WORLD 1945 CE TO 2000 CE.pdf',
                     'BA/SEM 5/HISTORY/TYBA HISTORY SEM V NOV 2022 - HISTORY OF MARATHAS 1630CE TO 1707CE.pdf',
                     'BA/SEM 5/HISTORY/TYBA HISTORY SEM V NOV 2022 - HISTORY OF MEDIEVEL INDIA 1000 CE TO 1526 CE.pdf',
                     'BA/SEM 5/HISTORY/TYBA HISTORY SEM V NOV 2022 - HISTORY OF MODERN MAHARASHTRA 1818 CE TO 1960 CE.pdf',
                     'BA/SEM 5/HISTORY/TYBA HISTORY SEM V NOV 2022 - RESEARCH METHODOLOGY _ SOURCES OF HISTORY.pdf'
 
                    ]

        # Send the PDF file to the user
        delay_seconds = 10
        write_timeout=35
        read_timeout=20
        for pdf_path in pdf_paths:
                with open(pdf_path, 'rb') as file:
                    await context.bot.send_document(chat_id=chat_id, document=file)

        await context.bot.send_message(chat_id=chat_id, text="Six Marathi 👇")
        pdf_paths = ['BA/SEM 5/MARATHI/TYBA MARATHI SEM V  NOV 2022 - HISTORY OF MEDIEVAL MARATHI LITRATURE.pdf',
                     'BA/SEM 5/MARATHI/TYBA MARATHI SEM V NOV 2022 - HISTORY OF MEDIEVAL MARATHI LITRATURE.pdf',
                     'BA/SEM 5/MARATHI/TYBA MARATHI SEM V NOV 2022 - INDIAN _ WESTERN THEORIES OF LITERATURE-I.pdf',
                     'BA/SEM 5/MARATHI/TYBA MARATHI SEM V NOV 2022 - INDIAN _ WESTERN THEORIES OF LITERATURE-II.pdf',
                     'BA/SEM 5/MARATHI/TYBA MARATHI SEM V NOV 2022 - LITERATURE _ SOCIETY.pdf',
                     'BA/SEM 5/MARATHI/TYBA MARATHI SEM V NOV 2022 - LITERATURE _ SOCIETY-II.pdf'
                    ]

        # Send the PDF file to the user
        delay_seconds = 10
        write_timeout=35
        read_timeout=20
        for pdf_path in pdf_paths:
                with open(pdf_path, 'rb') as file:
                    await context.bot.send_document(chat_id=chat_id, document=file)

        await context.bot.send_message(chat_id=chat_id, text="Six RD 👇"),
        pdf_paths = ['BA/SEM 5/RD/TYBA RD SEM V NOV 2022 - AGRICULTURE _ IT_S SIGNIFICANCE IN RURAL DEVELOPMENT.pdf',
                     'BA/SEM 5/RD/TYBA RD SEM V NOV 2022 - AGRIICULTURE _ ITS SIGNIFIANCE IN RURAL DEVELOPMENT.pdf',
                     'BA/SEM 5/RD/TYBA RD SEM V NOV 2022 - APPLIED AGRICULTURE-II.pdf',
                     'BA/SEM 5/RD/TYBA RD SEM V NOV 2022 - APPLIED AGRICULTURE.pdf',
                     'BA/SEM 5/RD/TYBA RD SEM V NOV 2022 - EMERGING ISSUE IN RURAL DEVELOPMENT.pdf',
                     'BA/SEM 5/RD/TYBA RD SEM V NOV 2022 - RURAL MARKETING _ FINANCE - 3762 Rural Development Rural Marketing and Finance.pdf',
                     'BA/SEM 5/RD/TYBA RD SEM V NOV 2022 - RURAL MARKETING _ FINANCE.pdf',
                     'BA/SEM 5/RD/TYBA RD SEM V NOV 2022 - RURAL RESOURCE MANAGEMENT.pdf',
                     'BA/SEM 5/RD/TYBA RD SEM V NOV 2022 - SOCIAL WORK FOR RURAL DEVELOPMENT.pdf'
                    ]

        
    elif Standard == "BvocHC":
                await context.bot.send_message(chat_id=chat_id, text="Question papers 2023-24")
                pdf_paths = ['BVOC HC/SEM 5/BVOC HC - Gynecological Nursing.pdf',
                             'BVOC HC/SEM 5/BVOC HC - Hospitality.pdf',
                             'BVOC HC/SEM 5/BVOC HC - Medical Surgical Nursing - I.pdf',
                             'BVOC HC/SEM 5/BVOC HC - Medical Surgical Nursing-II.pdf',
                             'BVOC HC/SEM 5/BVOC HC - Midwifery.pdf',
                     ]
                
    elif Standard == "BvocHT":
                await context.bot.send_message(chat_id=chat_id, text="Question papers 2023-24")
                pdf_paths = ['BVOC HT/SEM 5/BVOC HT  - Gynecological Nursing.pdf',
                             'BVOC HT/SEM 5/BVOC HT  - Medical Surgical Nursing - I.pdf',
                             'BVOC HT/SEM 5/BVOC HT  - Medical Surgical Nursing-II.pdf',
                             'BVOC HT/SEM 5/BVOC HT - Hospitality.pdf',
                             'BVOC HT/SEM 5/BVOC HT - Midwifery.pdf',
                     ]
                
    elif Standard == "BBI":
                await context.bot.send_message(chat_id=chat_id, text="Question papers 2023-24")
                pdf_paths = ['BBI/SEM 5/TYBBI SEM V NOV 2022 - Auditing - I.pdf',
                             'BBI/SEM 5/TYBBI SEM V NOV 2022 - Business Ethics and CorporateGovernance.pdf',
                             'BBI/SEM 5/TYBBI SEM V NOV 2022 - Financial Reporting & Analysis.pdf',
                             'BBI/SEM 5/TYBBI SEM V NOV 2022 - International Banking and Finance - 10011168.pdf',
                             'BBI/SEM 5/TYBBI SEM V NOV 2022 - Research Methodology.pdf',
                             'BBI/SEM 5/TYBBI SEM V NOV 2022 - Strategic Management.pdf'
                     ]
                
    elif Standard == "BMS" :
                await context.bot.send_message(chat_id=chat_id, text="Question papers 2023-24")
                pdf_paths = ['BMS/SEM 5/TYBMS  - FINANCE - WEALTH MANAGEMENT.pdf',
                             'BMS/SEM 5/TYBMS - CORPORATE COMMUNICATION & PUBLIC RELATIONS.pdf',
                             'BMS/SEM 5/TYBMS - FINANCE - FINANCIAL ACCOUNTING.pdf',
                             'BMS/SEM 5/TYBMS - FINANCE - INVESTMENT ANALYSIS & PORTFOLIO MANAGEMENT.pdf',
                             'BMS/SEM 5/TYBMS - FINANCE -DIRECT TAX.pdf',
                             'BMS/SEM 5/TYBMS - LOGISTIC & SUPPLY CHAIN MANAGEMENT.pdf',
                             'BMS/SEM 5/TYBMS - MARKETING - CUSTOMER RELATIONSHIP MANAGEMENT.pdf',
                             'BMS/SEM 5/TYBMS - MARKETING - E COMMERCE & DIGITAL MARKETING.pdf',
                             'BMS/SEM 5/TYBMS - MARKETING - SALES & DISTRIBUTION MANAGEMENT.pdf',
                             'BMS/SEM 5/TYBMS - MARKETING - SERVICE MARKETING.pdf'
                     ]
                
    elif Standard == "BCOM":
                await context.bot.send_message(chat_id=chat_id, text="Question papers 2023-24")
                pdf_paths = ['BCOM/SEM 5/TYBCOM  -  DIRECT & INDIRECT TAXATION.pdf',
                             'BCOM/SEM 5/TYBCOM  - COMMERCE V.pdf',
                             'BCOM/SEM 5/TYBCOM - BUSINESS ECONOMICS - V.pdf',
                             'BCOM/SEM 5/TYBCOM - COST ACCOUNTING.pdf',
                             'BCOM/SEM 5/TYBCOM - FINANCIAL ACCOUNTING & AUDITING X - COST ACCOUNTING.pdf',
                             'BCOM/SEM 5/TYBCOM - FINANCIAL ACCOUNTING AND AUDITING - VII.pdf',
                             'BCOM/SEM 5/TYBCOM - PURCHASING & STORE KEEPING.pdf'
                     ]

    elif Standard == "BSC":          
        await context.bot.send_message(chat_id=chat_id, text="BOTANY 👇")
        pdf_paths = ['BSC/SEM 5/BOTANY/TYBSC BOTANY SEM V NOV 2022 - CURRENT TRENDS IN PLANT SCIENCES II.pdf',
                     'BSC/SEM 5/BOTANY/TYBSC BOTANY SEM V NOV 2022 - FORM _ FUNCTION III.pdf',
                     'BSC/SEM 5/BOTANY/TYBSC BOTANY SEM V NOV 2022 - PLANT DIVERSITY III.pdf',
                     'BSC/SEM 5/BOTANY/TYBSC BOTANY SEM V NOV 2022 - PLANT DIVERSITY IV.pdf'
                    ]

        # Send the PDF file to the user
        delay_seconds = 10
        write_timeout=35
        read_timeout=20
        for pdf_path in pdf_paths:
                with open(pdf_path, 'rb') as file:
                    await context.bot.send_document(chat_id=chat_id, document=file)

        await context.bot.send_message(chat_id=chat_id, text="CHEMISTRY 👇")
        pdf_paths = ['BSC/SEM 5/CHEMISTRY/TYBSC CHEMISTRY SEM V NOV 2022 - ANALYTICAL CHEMISTRY.pdf',
                     'BSC/SEM 5/CHEMISTRY/TYBSC CHEMISTRY SEM V NOV 2022 - INORGANIC CHEMISTRY.pdf',
                     'BSC/SEM 5/CHEMISTRY/TYBSC CHEMISTRY SEM V NOV 2022 - ORGANIC CHEMISTRY.pdf',
                     'BSC/SEM 5/CHEMISTRY/TYBSC CHEMISTRY SEM V NOV 2022 - PHYSICAL CHEMISTRY.pdf'
                    ]

        # Send the PDF file to the user
        delay_seconds = 10
        write_timeout=35
        read_timeout=20
        for pdf_path in pdf_paths:
                with open(pdf_path, 'rb') as file:
                    await context.bot.send_document(chat_id=chat_id, document=file)

        await context.bot.send_message(chat_id=chat_id, text="PHYSICS 👇")
        pdf_paths = ['BSC/SEM 5/PHYSICS/TYBSC PHYSICS SEM V NOV 2022 - AUTOMIC _ MOLECULAR PHYSICS.pdf',
                     'BSC/SEM 5/PHYSICS/TYBSC PHYSICS SEM V NOV 2022 - ELECTRODYNAMICS.pdf',
                     'BSC/SEM 5/PHYSICS/TYBSC PHYSICS SEM V NOV 2022 - MATHEMATICAL, THARMAL AND STATISTICAL PHYSICS.pdf',
                     'BSC/SEM 5/PHYSICS/TYBSC PHYSICS SEM V NOV 2022 - SOLID STATE PHYSICS.pdf'
                    ]
                
    elif Standard == "BSCIT":
                pdf_paths = ['BSC IT/SEM 5/TYBSC IT SEM V NOV 2022 - ADVANCED WEB PROGRAMMING.pdf',
                             'BSC IT/SEM 5/TYBSC IT SEM V NOV 2022 - ARTIFICIAL INTELIIGENCE.pdf',
                             'BSC IT/SEM 5/TYBSC IT SEM V NOV 2022 - ENTERPRISE JAWA.pdf',
                             'BSC IT/SEM 5/TYBSC IT SEM V NOV 2022 - INTERNET OF THINGS - 10010155.pdf',
                             'BSC IT/SEM 5/TYBSC IT SEM V NOV 2022 - SOFTWARE PROJECT MANAGEMENT.pdf'
                     ]

    # Send the PDF file to the user
    delay_seconds = 10
    write_timeout=35
    read_timeout=20
    for pdf_path in pdf_paths:
            with open(pdf_path, 'rb') as file:
                await context.bot.send_document(chat_id=chat_id, document=file)



async def SEM_6(update, context):
    # Get the chat ID
    chat_id = update.effective_chat.id

    # Initialize an empty list for pdf_paths
    pdf_paths = []
    if Standard == "BA":
        # Send the initial message only once
        await context.bot.send_message(chat_id=chat_id, text="Question papers 2023-24")

        await context.bot.send_message(chat_id=chat_id, text="Six Economics 👇")
        pdf_paths = ['BA/SEM 6/ECONOMICS/TYBA Economics Economics of Agricultural and Co-Operation-II.pdf',
                     'BA/SEM 6/ECONOMICS/TYBA Economics Advanced Macroeconomics-III.pdf',
                     'BA/SEM 6/ECONOMICS/TYBA Economics Research Methodology-II.pdf',
                     'BA/SEM 6/ECONOMICS/TYBA Economics Research Methodology-II (Rev.).pdf'
                    ]
        delay_seconds = 10
        write_timeout=35
        read_timeout=20
        for pdf_path in pdf_paths:
                with open(pdf_path, 'rb') as file:
                    await context.bot.send_document(chat_id=chat_id, document=file)

        await context.bot.send_message(chat_id=chat_id, text="Six English 👇")
        pdf_paths = ['BA/SEM 6/ENGLISH/TYBA  English 20th Century British Literature - II.pdf',
                     'BA/SEM 6/ENGLISH/TYBA English 16th to 18th Century English Literature - II.pdf',
                     'BA/SEM 6/ENGLISH/TYBA English 19th Century English Literature - II.pdf',
                     'BA/SEM 6/ENGLISH/TYBA English Drama and Theatre - II.pdf',
                     'BA/SEM 6/ENGLISH/TYBA English Grammar and Art of Writing - II.pdf',
                     'BA/SEM 6/ENGLISH/TYBA English Literary Criticism - II.pdf'
                    ]

        # Send the PDF file to the user
        delay_seconds = 10
        write_timeout=35
        read_timeout=20
        for pdf_path in pdf_paths:
                with open(pdf_path, 'rb') as file:
                    await context.bot.send_document(chat_id=chat_id, document=file)


        await context.bot.send_message(chat_id=chat_id, text="Six Geography 👇")
        pdf_paths = ['BA/SEM 6/GEOGRAPHY/TYBA Geography Biogeography.pdf',
                     'BA/SEM 6/GEOGRAPHY/TYBA Geography Economic Geography.pdf',
                     'BA/SEM 6/GEOGRAPHY/TYBA Geography Environmental Geography.pdf',
                     'BA/SEM 6/GEOGRAPHY/TYBA Geography Geography of Tourism and Recreation.pdf'   
                    ]

        # Send the PDF file to the user
        delay_seconds = 10
        write_timeout=35
        read_timeout=20
        for pdf_path in pdf_paths:
                with open(pdf_path, 'rb') as file:
                    await context.bot.send_document(chat_id=chat_id, document=file)

        await context.bot.send_message(chat_id=chat_id, text="Six History 👇")
        pdf_paths = ['BA/SEM 6/HISTORY/TYBA History History of Asia (1945 CE.-2000 CE).pdf',
                     'BA/SEM 6/HISTORY/TYBA History History of Contemporary India (1947-CE2000 CE).pdf',
                     'BA/SEM 6/HISTORY/TYBA History History of Meieval India (1526 CE - 1707CE ).pdf',
                     'BA/SEM 6/HISTORY/TYBA History History of the Marathas (1707 CE - 1818CE ).pdf',
                     'BA/SEM 6/HISTORY/TYBA History Introduction to Museology and Archival Science.pdf',
                     'BA/SEM 6/HISTORY/TYBA History Research Methodology and Sources of History..pdf'
                    ]

        # Send the PDF file to the user
        delay_seconds = 10
        write_timeout=35
        read_timeout=20
        for pdf_path in pdf_paths:
                with open(pdf_path, 'rb') as file:
                    await context.bot.send_document(chat_id=chat_id, document=file)

        await context.bot.send_message(chat_id=chat_id, text="Six Marathi 👇")
        pdf_paths = ['BA/SEM 6/MARATHI/TYBA 86585 - Marathi Literature and Society.pdf',
                     'BA/SEM 6/MARATHI/TYBA Marathi History of Medieval Marathi Lit..pdf',
                     'BA/SEM 6/MARATHI/TYBA Marathi Indian _ Western Theories of Lit..pdf',
                     'BA/SEM 6/MARATHI/TYBA Marathi Literature and Society.pdf'
                    ]

        # Send the PDF file to the user
        delay_seconds = 10
        write_timeout=35
        read_timeout=20
        for pdf_path in pdf_paths:
                with open(pdf_path, 'rb') as file:
                    await context.bot.send_document(chat_id=chat_id, document=file)

        await context.bot.send_message(chat_id=chat_id, text="Six RD 👇"),
        pdf_paths = ['BA/SEM 6/RD/TYBA Rural Development Agriculture and its significance in Rural Development (2).pdf',
                     'BA/SEM 6/RD/TYBA Rural Development Agriculture and its significance in Rural Development.pdf',
                     'BA/SEM 6/RD/TYBA Rural Development Applied Agriculture (2).pdf',
                     'BA/SEM 6/RD/TYBA Rural Development Applied Agriculture.pdf',
                     'BA/SEM 6/RD/TYBA Rural Development Rural marketing and Finance.pdf',
                     'BA/SEM 6/RD/TYBA Rural Development Rural Resource Management.pdf',
                     'BA/SEM 6/RD/TYBA Rural Development Social work for Rural Development.pdf'
                    ]
    
    
    elif Standard == "BvocHC":
        await context.bot.send_message(chat_id=chat_id, text="Sorry, we don't have Semester Four PDFs available right now.")

    elif Standard == "BvocHT":
        await context.bot.send_message(chat_id=chat_id, text="Sorry, we don't have Semester Four PDFs available right now.")
        
    elif Standard == "BBI":
        await context.bot.send_message(chat_id=chat_id, text="Question papers 2023-24")
        pdf_paths = ['BBI/SEM 6/BBI  - International Business.pdf',
                     'BBI/SEM 6/BBI  85503 - Auditing - II.pdf',
                     'BBI/SEM 6/BBI - Central Banking.pdf',
                     'BBI/SEM 6/BBI - Human Resource Management.pdf',
                     'BBI/SEM 6/BBI - Security Analysis and Portfolio Management.pdf'
                     ]
        
    elif Standard == "BMS":
        await context.bot.send_message(chat_id=chat_id, text="Question papers 2023-24")
        pdf_paths = ['BMS/SEM 6/BMS - Elective Finance Financing Rural Development.pdf',
                     'BMS/SEM 6/BMS - Elective Finance Indirect Taxes.pdf',
                     'BMS/SEM 6/BMS - Elective Finance Innovative Financial Services.pdf',
                     'BMS/SEM 6/BMS - Elective Marketing Retail Management.pdf',
                     'BMS/SEM 6/BMS - Finance Strategic Financial Management.pdf',
                     'BMS/SEM 6/BMS - Marketing International Marketing.pdf',
                     'BMS/SEM 6/BMS - Marketing Media Planning & Management.pdf',
                     'BMS/SEM 6/BMS - MarketingBrand Management.pdf',
                     'BMS/SEM 6/BMS - Operation Research.pdf',
                     ]
        
    elif Standard == "BCOM":
        await context.bot.send_message(chat_id=chat_id, text="Question papers 2023-24")
        pdf_paths = ['BCOM/SEM 6/TYBCom  - Commerce VI.pdf',
                     'BCOM/SEM 6/TYBCom - Business Economics VI.pdf',
                     'BCOM/SEM 6/TYBCom - Direct & Indirect Taxation Paper - II.pdf',
                     'BCOM/SEM 6/TYBCom - Financial Accounting and Auditing X - Cost Accounting.pdf',
                     'BCOM/SEM 6/TYBCom - Purchasing & Store keeping Paper - II.pdf',
                     'BCOM/SEM 6/TYBCom VI Financial accounting & auditing paper IX financial accounting.pdf',
                     ]
        
    elif Standard == "BSC":          
        await context.bot.send_message(chat_id=chat_id, text="BOTANY 👇")
        pdf_paths = ['BSC/SEM 6/BOTANY/TYBSC - Botany Current Trends in Plant Sciences II.pdf',
                     'BSC/SEM 6/BOTANY/TYBSC - Botany Plant Diversity III (R-2020).pdf',
                     'BSC/SEM 6/BOTANY/TYBSC - Botany Plant Diversity IV (R-2020).pdf',
                     'BSC/SEM 6/BOTANY/TYBSC - Botany Form _ Function III (R-2020).pdf'
                    ]

        # Send the PDF file to the user
        delay_seconds = 10
        write_timeout=35
        read_timeout=20
        for pdf_path in pdf_paths:
                with open(pdf_path, 'rb') as file:
                    await context.bot.send_document(chat_id=chat_id, document=file)

        await context.bot.send_message(chat_id=chat_id, text="CHEMISTRY 👇")
        pdf_paths = ['BSC/SEM 6/CHEMISTRY/TYBSC - Chemistry Analytical Chemistry (6 Units).pdf',
                     'BSC/SEM 6/CHEMISTRY/TYBSC - Chemistry Inorganic Chemistry (6 Units).pdf',
                     'BSC/SEM 6/CHEMISTRY/TYBSC - Chemistry Analytical Chemistry (6 Units).pdf',
                     'BSC/SEM 6/CHEMISTRY/TYBSC - Chemistry Organic Chemistry (6 Units).pdf'
                    ]

        # Send the PDF file to the user
        delay_seconds = 10
        write_timeout=35
        read_timeout=20
        for pdf_path in pdf_paths:
                with open(pdf_path, 'rb') as file:
                    await context.bot.send_document(chat_id=chat_id, document=file)

        await context.bot.send_message(chat_id=chat_id, text="PHYSICS 👇")
        pdf_paths = ['BSC/SEM 6/PHYSICS/TYBSC - Physics Classical Mechanics.pdf',
                     'BSC/SEM 6/PHYSICS/TYBSC - Physics Electronics.pdf',
                     'BSC/SEM 6/PHYSICS/TYBSC - Physics Special Theory of Relativity.pdf',
                     'BSC/SEM 6/PHYSICS/TYBSC - Physics Nuclear Physics.pdf'
                    ]
    elif Standard == "BSCIT":
        await context.bot.send_message(chat_id=chat_id, text="Question papers 2023-24")
        pdf_paths = ['BSC IT/SEM 6/BSC IT - Business Intellitgence.pdf',
                     'BSC IT/SEM 6/BSC IT - I. T. Service Management.pdf',
                     'BSC IT/SEM 6/BSC IT - Principles of Geographic Information Systems.pdf',
                     'BSC IT/SEM 6/BSC IT - Quality Assurance.pdf',
                     'BSC IT/SEM 6/BSC IT - Security in Computing.pdf'
                     ]

    # Send the initial message only once
    # await context.bot.send_message(chat_id=chat_id, text="Question papers 2023-24")

    # Send the PDF file to the user
    delay_seconds = 10
    write_timeout=35
    read_timeout=20
    for pdf_path in pdf_paths:
            with open(pdf_path, 'rb') as file:
                await context.bot.send_document(chat_id=chat_id, document=file)





    
if __name__ == '__main__':
    app = Application.builder().token(Token).build()

    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler("BA", BA))
    app.add_handler(CommandHandler("BvocHC", BvocHC))
    app.add_handler(CommandHandler("BvocHT", BvocHT))
    app.add_handler(CommandHandler("BCOM", BCOM))
    app.add_handler(CommandHandler("BBI", BBI))
    app.add_handler(CommandHandler("BMS", BMS))
    app.add_handler(CommandHandler("BSC", BSC))
    app.add_handler(CommandHandler("BSCIT", BSCIT))
    app.add_handler(CommandHandler("FY", FY))
    app.add_handler(CommandHandler("SY", SY))
    app.add_handler(CommandHandler("SEM_1", SEM_1))
    app.add_handler(CommandHandler("SEM_2", SEM_2))
    app.add_handler(CommandHandler("SEM_3", SEM_3))
    app.add_handler(CommandHandler("SEM_4", SEM_4))
    app.add_handler(CallbackQueryHandler(button_clicked))
    # app.add_handler(CallbackQueryHandler(std_button_clicked))



    app.run_polling()


