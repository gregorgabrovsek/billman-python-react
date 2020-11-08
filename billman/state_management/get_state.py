from billman.state_management.state import *
from datetime import datetime, timedelta

state = State(
    users=[
        User(
            id=0,
            name="Peppa",
            surname="Pig",
            address="Čokoladna ulica nekje",
            banc_acc_number="SI56293847932865923",
            local_credit="3.1",
            family={1, 2}
        ),
        User(
            id=1,
            name="George",
            surname="Pig",
            address="Disneyland 16a",
            banc_acc_number="SI563548463245356",
            local_credit="8327947197",
            family={0, 2}
        ),
        User(
            id=2,
            name="Mummy",
            surname="Pig",
            address="Lonček 113",
            banc_acc_number="SI563453636865923",
            local_credit="50.50",
            family={0, 1}
        )
    ],
    categories=[
        Category(name="Family"),
        Category(name="Food"),
        Category(name="Fun"),
        Category(name="Education"),
        Category(name="Sport"),
        Category(name="Transport"),
        Category(name="Fixed expenses"),
        Category(name="Community"),
        Category(name="Other"),
    ],
    community=[
        Community(id=0, goal=100.5, collected=50.25, cause="Družini vidmajer je toča uničila streho. Pomagajte!"),
        Community(id=1, goal=800.0, cause="Omogočimo otrokom izlet v Črno goro!"),
        Community(id=2, goal=150, cause="Zbiramo sredstva za male živali..."),
        Community(id=3, goal=1054.52, collected=72, cause="Gregor, Maja in Barbara so lačni. Darujte!"),
        Community(id=4, goal=100, collected=100, cause="Stara mama Helga zbira denar za flamethrower7000"),
    ],
    bills=[
        Bill(
            id=0,
            id_payer=0,
            short_name="univerzalj",
            category="Education",
            reference="SI12",
            date_payment="",  # ni placan - prazen string
            date_due="2020-11-12",
            date_issued="2020-10-12",
            total=21.02,
            purpose="Vpisnina",
            code_purpose="STDY",
            recipient="Univerza v Ljubljani",
            recipient_address="Kongresni trg 12, 1000 Ljubljana",
            BIC_bank_recipient="ABCD1234",
            IBAN_recipient="SI32124578563456789",
            visible_family="True"
        ),
        Bill(
            id=1,
            id_payer=0,
            short_name="ilirija",
            category="Sport",
            reference="SI15",
            date_payment="2020-11-05",
            date_due="2020-12-11",
            date_issued="2020-10-12",
            total=32.00,
            purpose="Članarina za plavalni klub",
            code_purpose="MDCS",
            recipient="Plavalni klub Ilirija",
            recipient_address="Celovška cesta 3, 1000 Ljubljana",
            BIC_bank_recipient="ABCD7634",
            IBAN_recipient="SI32124578563443210",
            visible_family="True"
        ),
        Bill(
            id=2,
            id_payer=0,
            short_name="lpp",
            category="Transport",
            reference="SI20",
            date_payment="2020-11-01",
            date_due="2021-01-01",
            date_issued="2020-11-06",
            total=210.00,
            purpose="IJPP",
            code_purpose="BUSB",
            recipient="LPP d.o.o.",
            recipient_address="Celovška cesta 160, 1000 Ljubljana",
            BIC_bank_recipient="EFGH3134",
            IBAN_recipient="SI32134988563443210",
            visible_family="True"
        ),
        Bill(
            id=3,
            id_payer=2,
            short_name="petrol",
            category="Fun",
            reference="SI20",
            date_payment="",  # ni placan - prazen string
            date_due="2021-11-11",
            date_issued="2020-07-12",
            total=17.64,
            purpose="Concert tickets",
            code_purpose="OTHR",
            recipient="Petrol d.d.",
            recipient_address="Dunajska cesta 50, 1000 Ljubljana",
            BIC_bank_recipient="EX6K3134",
            IBAN_recipient="SI32134988563654321",
            visible_family="True"
        ),
        Bill(
            id=4,
            id_payer=1,
            short_name="t2",
            category="Other",
            reference="SI11",
            date_payment="",
            date_due="2021-03-04",
            date_issued="2020-05-12",
            total=5560.69,
            purpose="Internetne storitve",
            code_purpose="OTHR",
            recipient="T-2 d.o.o.",
            recipient_address="Verovškova 64a, 1000 Ljubljana",
            BIC_bank_recipient="XLBA5174",
            IBAN_recipient="SI54789885636543218",
            visible_family="True"
        ),
        Bill(
            id=5,
            id_payer=0,
            short_name="petrol",
            category="Transport",
            reference="SI20",
            date_payment="",  # ni placan - prazen string
            date_due="2020-11-08",
            date_issued="2020-10-12",
            total=112.00,
            purpose="Letna vinjeta",
            code_purpose="OTHR",
            recipient="Petrol d.d.",
            recipient_address="Dunajska cesta 50, 1000 Ljubljana",
            BIC_bank_recipient="EX6K3134",
            IBAN_recipient="SI32134988563654321",
            visible_family="True"
        ),
        Bill(
            id=6,
            id_payer=0,
            short_name="t2",
            category="Other",
            reference="SI11",
            date_payment="",
            date_due="2021-11-08",
            date_issued="2020-08-12",
            total=5560.69,
            purpose="Nakup opreme",
            code_purpose="OTHR",
            recipient="T-2 d.o.o.",
            recipient_address="Verovškova 64a, 1000 Ljubljana",
            BIC_bank_recipient="XLBA5174",
            IBAN_recipient="SI54789885636543218",
            visible_family="True"
        )
    ],
)


async def get_state() -> State:
    return state


def get_byCategory(cat):
    categoryBills = []
    for bill in state.bills:
        if bill.category == cat:
            categoryBills.append(bill)
    return categoryBills


def get_billDateDue():
    dueDateBills = []
    for bill in state.bills:
        if bill.date_payment == "":
            dueDateBills.append(bill)
    dueDateBills.sort(key=lambda r: r.date_due, reverse=True)
    return dueDateBills


def get_billDatePayed():
    payedDateBills = []
    for bill in state.bills:
        if bill.date_payment != "":
            payedDateBills.append(bill)
    payedDateBills.sort(key=lambda r: r.date_payment, reverse=True)
    return payedDateBills


def get_byTotalAsc():
    billsAsc = state.bills
    billsAsc.sort(key=lambda r: r.total)
    return billsAsc


def get_byTotalDesc():
    billsDesc = state.bills
    billsDesc.sort(key=lambda r: r.total, reverse=True)
    return billsDesc


def get_family(option):
    seen = []
    for bill in state.bills:
        if bill.visible_family == option:
            seen.append(bill)
    seen.sort(key=lambda r: r.date_due)
    return seen


def set_billPaid(id_bill, credits):
    for bill in state.bills:
        if bill.id == id_bill:
            if credits:
                state.users[0].local_credit -= bill.total
            bill.date_payment = str(datetime.today().strftime('%Y-%m-%d'))
            break
    return


def set_transactCredits(id_recipient, amount):
    for user in state.users:
        if user.id == id_recipient:
            user.local_credit += amount
            state.users[0].local_credit -= amount
            break
    return


def create_community_bill(cause_id, amount) -> int:
    today = datetime.now()
    date_today = today.strftime("%Y-%m-%d")
    date_due = (today + timedelta(14)).strftime("%Y-%m-%d")
    cause = "Provide help"
    for com in state.community:
        if com.id == cause_id:
            cause = com.cause
            # ker bomo takoj placali ta racun, lahko ze v community povisamo zbrani znesek
            com.collected += amount

    new_bill = Bill(id=8,
                    id_payer=0,
                    short_name="community",
                    category="Community",
                    reference="SI11",
                    date_payment="",
                    date_due=date_due,
                    date_issued=date_today,
                    total=amount,
                    purpose=cause,
                    code_purpose="HELP",
                    recipient="Humanitarno društvo",
                    recipient_address="Ozka ulica 54, 1200 Moravče",
                    BIC_bank_recipient="ERG23422",
                    IBAN_recipient="SI5614134325235",
                    visible_family=False
                    )
    state.bills.append(new_bill)
    return new_bill.id


def create_user_plus_from_user(user) -> UserPlus:
    new_user_plus = UserPlus(
        id=user.id,
        name=user.name,
        surname=user.surname,
        address=user.address,
        banc_acc_number=user.banc_acc_number,
        local_credit=user.local_credit,
        family=user.family,
        family_bills=[]
    )
    for bill in state.bills:
        if bill.id_payer == user.id and bill.date_payment == "" and bill.visible_family:
            new_user_plus.family_bills.append(bill)
    return new_user_plus
