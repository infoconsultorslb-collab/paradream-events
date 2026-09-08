#!/usr/bin/env python3
"""
Generates the static Paradream Events site (HTML pages) from the content
extracted out of the old Strikingly-hosted site. Run with:
    python3 tools/build.py
from the repo root. Regenerates every .html file in the repo (except files
under assets/), so it's safe to re-run after editing the DATA below.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Optional path prefix for hosting under a subfolder (e.g. GitHub Pages project
# sites at github.io/<repo>/). Leave unset (empty) for a domain-root deploy
# like Netlify/Vercel/the real paradreamlb.com.
BASE = os.environ.get("PARADREAM_BASE", "").rstrip("/")

SITE_NAME = "Paradream Events"
TAGLINE = "YOU DREAM, WE ACHIEVE"
PHONE = "+961 81 406046"
PHONE_HREF = "tel:+96181406046"
EMAIL = "paradreamlb@gmail.com"
INSTAGRAM = "https://www.instagram.com/paradream.lb"
FACEBOOK = "https://www.facebook.com/share/1Aus8ErrkL/"
ADDRESS = "Furn El Chebbak, Beirut, Lebanon"

NAV_LINKS = [
    ("/", "Home"),
    ("/why-paradream.html", "Why Paradream?"),
    ("/our-services.html", "Our Services"),
    ("/gallery.html", "Gallery"),
    ("/contact-us.html", "Contact Us"),
]

EVENTS = [
    ("proposal", "Proposal"),
    ("engagement", "Engagement"),
    ("bachelor", "Bachelor"),
    ("your-big-day", "Your Big Day (Wedding)"),
    ("holy-first-communion", "Holy First Communion"),
    ("baptism", "Baptism"),
    ("gender-reveal", "Gender Reveal"),
    ("birthday", "Birthday"),
    ("christmas", "Christmas"),
]

PORTFOLIO = [
    ("oriental-zaffah", "Oriental Zaffah", "676820_523291"),
    ("circus-show", "Circus Show", "45371_778378"),
    ("inflatable-games", "Inflatable Games", "22742_446239"),
    ("table-decoration-set-up", "Table Decoration Set-Up", "467059_169031"),
    ("catering-services", "Catering Services", "808874_30317"),
    ("characters-mascots", "Characters & Mascots", "749843_688071"),
    ("photo-booth-entertainment", "Photo Booth Entertainment", "809940_597500"),
    ("christmas-mascots", "Christmas Mascots", "853097_675776"),
]

PORTFOLIO_IMAGES = {
    "catering-services": ["199750_677009","554347_576343","436687_349758","281761_711233","118565_804332","401246_8970","592135_480536","398140_262336","747725_418256","305089_805392","823101_548286","911439_141851","669723_27325","719927_723809","684438_553321","349198_372830","619190_963679","746668_379246"],
    "characters-mascots": ["749843_688071","479156_558716","558113_319985","255126_886521","474959_810716","853402_493806","677244_69652","314521_285884","254241_279922","402611_650812","598874_627614","851143_368948","498663_357934","550565_568436","557100_99972","779897_996018","392410_605535","194976_232330","5647_633439","862712_746063"],
    "christmas-mascots": ["853097_675776","429295_213563","98990_325783","314113_400307","428737_407378","739830_401521","70658_619291"],
    "circus-show": ["45371_778378","587260_992861","314518_666679","197051_547608","281772_834395","708100_315319","5811_142534","773369_896272"],
    "inflatable-games": ["22742_446239","498718_313472","821423_810146","217752_650457","458146_795811","346348_65294","550593_51624","777823_434989","870528_234765","238241_337729","631017_932532","775844_157998","20285_532670","429599_397546","59884_856255","781239_176190","200392_404472","714498_432449","863586_62590","577558_913390","470642_531882","946398_564759","92434_407529","415514_169424","61635_519356","135458_89690","652548_221706","476005_426814","57530_964333","542848_478570","897570_52586","94301_753759","495164_395296","260094_498970","361290_431603","605267_357133","977004_628155","963806_652672","760930_251593","209940_927686","908118_497468","30157_185178","124967_452933","356784_558483","371949_125313"],
    "oriental-zaffah": ["676820_523291","56013_414516","446518_376324","585565_811871","805875_551064","196224_409767","609048_561303","578796_14209","362950_370626","543579_227308"],
    "photo-booth-entertainment": ["809940_597500","103465_541357","603488_645729","656177_713884","693028_596462","389230_501191","861120_898696","663051_660924","97325_12362","802962_484008","946104_219888","559497_662792","509944_956912","867626_643797"],
    "table-decoration-set-up": ["467059_169031","581960_938824","472642_187916","31524_29344","671446_918275","768911_493585","276458_181229","930214_392523","77378_424488","909449_124171","878787_304110","874801_714126","29744_206386","462981_13576","59098_285443","734814_702898","162747_31284","231359_929980","888278_185053","463581_438862"],
}

GALLERY_IMAGES = ["299789_805561","627314_84116","402611_650812","83913_522050","779897_996018","327623_961035","45371_778378","5811_142534","853097_675776","314518_666679","197051_547608","558113_319985","708100_315319","773369_896272","739830_401521","677244_69652","933492_22247","213053_283820","990452_463366","281772_834395","148879_949972","547817_309673","609048_561303","195494_515473","194976_232330","742677_776834","255126_886521","151607_382593","641639_75867","862712_746063","550565_568436","70658_619291","692411_160382","474959_810716","576619_113012","600458_459146","557100_99972","153622_139741","851143_368948","223289_457332","498663_357934","335988_271880","479156_558716","949922_866581","667350_788609","598874_627614","97989_403012","98990_325783","557137_689745","5647_633439","584124_920207","749843_688071","299026_4471","428737_407378","267670_286274","429295_213563","689735_28783","86719_615249","930825_474201","684558_868848","372577_743429","370910_834396","392410_605535","103819_771341","915964_75053","314113_400307","527639_744484","254241_279922","314521_285884","159572_227299","973512_577868","874365_41016","853402_493806","984285_738332","527189_950340","749781_426983","868552_562390","899805_596197","949209_699999","689070_524598","915771_484512"]

TESTIMONIAL_IMAGES = ["159401_417278","327623_961035","220930_341269","285581_545397","225122_87972","588520_558441"]

TESTIMONIALS = [
    ("Mitri & Sethrida's Wedding", "From our proposal to our wedding, Paradream exceeded every expectation. We had a clear vision, and they brought it to life flawlessly—the mood board was executed exactly as we imagined. The atmosphere was electric, everyone was dancing and celebrating with joy. It truly felt like a dream. I confidently recommend Paradream to anyone planning a special event; they made our moments unforgettable."),
    ("Jean-Marie & Lili's Engagement", "I still get chills thinking about our engagement night—Paradream turned it into absolute MAGIC! From the moment we stepped in, it felt like we were living inside a fairytale. The setup was breathtaking, the entertainment was next-level, and the vibe? Unmatched. Every guest was blown away, and we were speechless. If you're planning an engagement, don’t even think twice. Book Paradream now—they don’t just plan events, they create unforgettable moments you’ll cherish forever!"),
    ("Bruna's Birthday", "I honestly couldn’t believe it—they actually made it happen! My birthday felt like a dream come true. Even though I was far away, Paradream showed up to celebrate with me, and turned a regular day into something unforgettable. It started as a surprise, but since then, they’ve become a part of every celebration in my life. Their energy, their team, their beautiful spirit—Paradream doesn’t just show up, they light up the entire occasion. I wouldn’t celebrate without them!"),
    ("Exquitech Christmas Gathering", "“Paradream transformed our vision into a truly unforgettable experience. From the first idea to the final execution, their team showed exceptional creativity, professionalism, and attention to detail. We want to express our sincere gratitude to Paradream for their dedication and for making our event so meaningful and seamless. Choosing them was the best decision we could have made.”"),
    ("SOS End Of Project", "This Christmas, we had the honor of turning a meaningful dream into reality by supporting an organization as inspiring as SOS Children’s Village. We are deeply grateful for the opportunity to collaborate with such a remarkable children’s center and contribute to its heartfelt mission. Moments like these reinforce why Paradream proudly stands as one of the leading event planning and entertainment agencies in Lebanon."),
]

OCCASIONS = [
    ("proposal", "Proposal", "The proposal is a once-in-a-lifetime moment, and we specialize in crafting unforgettable experiences that ensure a perfect and memorable “yes” moment."),
    ("engagement", "Engagement", "Celebrate your love story with our bespoke engagement event services. Our team of experienced planners will work closely with you to bring your dream to life, from intimate moments to grand gestures."),
    ("bachelor", "Bachelor", "Experience an exceptional bachelor party with our elite planning services. We create sophisticated, tailored celebrations, handling every detail from curated activities to premium entertainment."),
    ("your-big-day", "Your Big Day", "Make your dream wedding come true with Paradream. Our expert planning transforms your vision into a flawlessly executed celebration that you’ll treasure forever."),
    ("holy-first-communion", "Holy First Communion", "Your child’s First Communion deserves to be a truly exceptional and memorable event, planned with detail and a touch of spiritual sophistication."),
    ("baptism", "Baptism", "Your child’s Baptism is a sacred milestone that calls for a warm, heartfelt celebration. We create a serene and joyful atmosphere that honors this blessed day."),
    ("gender-reveal", "Gender Reveal", "The sweetest suspense of all — boy or girl, we celebrate with sparkle and surprise! Every gender reveal is a magical moment, filled with joy, love, and a burst of color."),
    ("birthday", "Birthday", "Choose Paradream to make your birthday truly unforgettable, ensuring a seamless and exceptional experience that will leave a lasting impression on you and your guests."),
    ("christmas", "Christmas", "Christmas is the dreaming season — better together! Music at Christmas time is like no other, enchanting hearts and weaving joy into the air. P.S. ask Santa Claus for Paradream!"),
]

# ---------------------------------------------------------------------------

def img(id_ext, alt="", cls="", loading="lazy"):
    return f'<img src="{BASE}/assets/img/{id_ext}" alt="{alt}" class="{cls}" loading="{loading}">'

def find_img(iid):
    for ext in ("jpg", "jpeg", "png"):
        if os.path.exists(os.path.join(ROOT, "assets", "img", f"{iid}.{ext}")):
            return f"{iid}.{ext}"
    return f"{iid}.jpg"

def page(title, description, body, canonical="/", extra_head=""):
    nav_items = "".join(
        f'<li><a href="{BASE}{href}">{label}</a></li>' for href, label in NAV_LINKS
    )
    events_items = "".join(
        f'<li><a href="{BASE}/events/{slug}.html">{label}</a></li>' for slug, label in EVENTS
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="https://www.paradreamlb.com{canonical}">
<link rel="icon" href="{BASE}/assets/img/{find_img('642152_189371')}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{BASE}/assets/img/{find_img('376585_257154')}">
<meta property="og:type" content="website">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800&amp;family=Source+Sans+Pro:ital,wght@0,400;0,600;0,700;1,400&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="{BASE}/assets/css/style.css">
{extra_head}
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="{BASE}/">
      <img src="{BASE}/assets/img/{find_img('43580_800970')}" alt="{SITE_NAME}" class="brand-logo">
      <span class="brand-name">{SITE_NAME}</span>
    </a>
    <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false" aria-controls="site-nav">
      <span></span><span></span><span></span>
    </button>
    <nav class="site-nav" id="site-nav">
      <ul class="nav-primary">
        {nav_items}
        <li class="has-dropdown">
          <a href="{BASE}/our-services.html">Book an Event <span class="caret">&#9662;</span></a>
          <ul class="dropdown">{events_items}</ul>
        </li>
      </ul>
      <a class="btn btn-primary nav-cta" href="{BASE}/contact-us.html">Book Now</a>
    </nav>
  </div>
</header>

<main id="main">
{body}
</main>

<footer class="site-footer">
  <div class="wrap footer-inner">
    <div class="footer-col">
      <h4>{SITE_NAME}</h4>
      <p>{ADDRESS}</p>
      <p>+12 years experience in events, hospitality, and F&amp;B services!</p>
      <p><a href="{PHONE_HREF}">{PHONE}</a></p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <div class="social-links">
        <a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a>
        <a href="{FACEBOOK}" target="_blank" rel="noopener">Facebook</a>
      </div>
    </div>
    <div class="footer-col">
      <h4>Events</h4>
      <ul>
        {"".join(f'<li><a href="{BASE}/events/{slug}.html">{label}</a></li>' for slug, label in EVENTS)}
      </ul>
    </div>
    <div class="footer-col">
      <h4>Quick Links</h4>
      <ul>
        <li><a href="{BASE}/">Home</a></li>
        <li><a href="{BASE}/why-paradream.html">Why Paradream?</a></li>
        <li><a href="{BASE}/our-services.html">Our Services</a></li>
        <li><a href="{BASE}/gallery.html">Gallery</a></li>
        <li><a href="{BASE}/contact-us.html">Contact Us</a></li>
        <li><a href="{BASE}/join-us.html">Join Our Team</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap footer-bottom">
    <p>&copy; {2026} {SITE_NAME}. All rights reserved.</p>
    <a href="{BASE}/cookie-policy.html">Cookie Policy</a>
  </div>
</footer>

<div class="cookie-banner" id="cookie-banner" hidden>
  <p>We use cookies to ensure a smooth browsing experience. By continuing we assume you accept the use of cookies. <a href="{BASE}/cookie-policy.html">Learn More</a></p>
  <button class="btn btn-primary btn-sm" id="cookie-accept">Accept</button>
</div>

<script src="{BASE}/assets/js/main.js"></script>
</body>
</html>
"""

def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", path)

# ---------------------------------------------------------------------------
# Booking form field definitions per event (reconstructed from the original
# site's form schemas) rendered as real Netlify Forms.

GUESTS_OPTIONS = ["50 - 100", "100 - 200", "200 - 300", "300 - 400", "400 - 500", "500+"]
BUDGET_OPTIONS = ["500 - 1000 USD", "1000 - 2000 USD", "2000 - 3000 USD", "3000 - 4000 USD", "4000 - 5000 USD", "5000+ USD"]
CATERING_OPTIONS = ["Buffet", "Oriental Lebanese Mezza", "International Cuisine", "Live Cooking Station", "Food Truck", "Other"]
ENTERTAINMENT_GENERAL = ["Live Show Parade", "Live Show Zaffah", "Customized Music Show", "Glitter Show", "Glow In the Dark", "Bar Show", "Dj Show", "Firework", "Phone Recorder", "360° Photo Booth", "Mirror Photo Booth", "Characters & Mascots", "Science Show", "Magic Show", "Other"]
DECOR_GENERAL = ["Signs & Stands", "Balloons", "Flowers", "Customized Set-Up", "Milk Chocolate", "Dark Chocolate", "White Chocolate", "Dubai Chocolate", "Customized Chocolate", "Other"]
ENTERTAINMENT_CHRISTMAS = ["Christmas Parade", "Santa Claus Appearance", "Christmas Choir", "Live Christmas Show", "Elf Show", "Gift Distribution", "Tree Lighting Show", "Characters & Mascots", "Science Show", "Magic Show", "Glow In the Dark", "Other"]
DECOR_CHRISTMAS = ["Christmas Decoration", "Santa With Candies", "Milk Chocolate", "Dark Chocolate", "White Chocolate", "Candy Canes", "Bûches de Noël", "Other"]
ENTERTAINMENT_WEDDING = ["Live Show Parade", "Live Show Zaffah", "Playback Show", "Tabl Show", "Darbuka Show", "Violin Show", "Wind Instrument Show (Trumpet, Saxophone, Trombone)", "Piano Show", "Glitter Show", "Dj Show", "Bar Show", "Other"]
PACKAGES_WEDDING = ["Silver Package (50-100 pers)", "Bronze Package (100-200 pers)", "Gold Package (200-300 pers)", "Platinum Package (300+)", "Fake Cake", "Milk Chocolate", "Dark Chocolate", "White Chocolate", "Dubai Chocolate", "Other"]
CARDS_OPTIONS = ["Electronic Card", "Plexi Card", "Board Card", "Thank You Card", "Customized Card", "Cadeaux De Retour", "Other"]
VENUE_PREF_OPTIONS = ["Indoor", "Outdoor", "Panoramic Mountain View", "Beach Sunset", "Private Venue", "Other"]
SURPRISE_OPTIONS = ["Surprise", "Planned"]
DECOR_PROPOSAL = ["Will You Marry Me Signs", "Stands", "Balloons", "Flowers", "Customized Set-Up", "Milk Chocolate", "Dark Chocolate", "White Chocolate", "Dubai Chocolate", "Customized Chocolate", "Other"]
HEAR_ABOUT_OPTIONS = ["Instagram", "Facebook", "Google", "Friend / Family", "Other"]

def f_text(name, label, required=True):
    return {"kind": "text", "name": name, "label": label, "required": required}
def f_email(name="email", label="Email", required=True):
    return {"kind": "email", "name": name, "label": label, "required": required}
def f_tel(name="phone", label="Phone", required=True):
    return {"kind": "tel", "name": name, "label": label, "required": required}
def f_date(name="event_date", label="Date", required=True):
    return {"kind": "date", "name": name, "label": label, "required": required}
def f_select(name, label, options, required=True):
    return {"kind": "select", "name": name, "label": label, "options": options, "required": required}
def f_radio(name, label, options, required=True):
    return {"kind": "radio", "name": name, "label": label, "options": options, "required": required}
def f_checkboxes(name, label, options, required=False):
    return {"kind": "checkboxes", "name": name, "label": label, "options": options, "required": required}
def f_textarea(name, label, required=False):
    return {"kind": "textarea", "name": name, "label": label, "required": required}

NAME_FIELDS = [f_text("first_name", "First Name"), f_text("last_name", "Last Name")]

def basic_fields(catering=CATERING_OPTIONS, entertainment=ENTERTAINMENT_GENERAL, decor=DECOR_GENERAL, decor_label="Chocolate & Decoration"):
    return [
        *NAME_FIELDS,
        f_email(),
        f_tel(),
        f_text("venue_address", "Venue Address", required=False),
        f_date(),
        f_select("guests", "Estimated Guests", GUESTS_OPTIONS),
        f_select("budget", "Budget Range", BUDGET_OPTIONS),
        f_select("catering", "Catering Selection", catering),
        f_checkboxes("entertainment", "Entertainment", entertainment),
        f_checkboxes("decoration", decor_label, decor),
        f_textarea("notes", "Special Instructions"),
    ]

EVENT_FORMS = {
    "proposal": [
        *NAME_FIELDS, f_email(), f_tel(),
        f_text("venue_address", "Venue Address", required=False),
        f_date(),
        f_radio("style", "Surprise or Planned", SURPRISE_OPTIONS),
        f_select("guests", "Estimated Guests", GUESTS_OPTIONS),
        f_select("budget", "Budget Range", BUDGET_OPTIONS),
        f_select("catering", "Catering Selection", CATERING_OPTIONS),
        f_checkboxes("entertainment", "Entertainment", ENTERTAINMENT_GENERAL),
        f_checkboxes("decoration", "Chocolate & Decoration", DECOR_PROPOSAL),
        f_textarea("notes", "Special Instructions"),
    ],
    "engagement": basic_fields(),
    "bachelor": [
        *NAME_FIELDS, f_email(), f_tel(),
        f_text("venue_address", "Venue Address", required=False),
        f_date(),
        f_radio("style", "Surprise or Planned", SURPRISE_OPTIONS),
        f_select("guests", "Estimated Guests", GUESTS_OPTIONS),
        f_select("budget", "Budget Range", BUDGET_OPTIONS),
        f_select("catering", "Catering Selection", CATERING_OPTIONS),
        f_checkboxes("entertainment", "Entertainment", ENTERTAINMENT_GENERAL),
        f_checkboxes("decoration", "Chocolate & Decoration", DECOR_GENERAL),
        f_textarea("notes", "Special Instructions"),
    ],
    "your-big-day": [
        f_text("bride_name", "Bride Name"), f_text("bride_age", "Bride Age", required=False),
        f_text("groom_name", "Groom Name"), f_text("groom_age", "Groom Age", required=False),
        f_email(), f_tel(),
        f_date(),
        f_radio("venue_booked", "Booked A Venue?", ["Yes", "Still Looking", "We Need Help"]),
        f_checkboxes("venue_pref", "Venue Preferences", VENUE_PREF_OPTIONS),
        f_select("catering", "Catering Selection", CATERING_OPTIONS + ["Mediterranean Cuisine"]),
        f_checkboxes("entertainment", "Entertainment", ENTERTAINMENT_WEDDING),
        f_checkboxes("packages", "Packages, Cake & Chocolate", PACKAGES_WEDDING),
        f_checkboxes("cards", "Cards", CARDS_OPTIONS),
        f_textarea("notes", "Special Instructions"),
    ],
    "holy-first-communion": basic_fields(),
    "baptism": basic_fields(),
    "gender-reveal": basic_fields(),
    "birthday": basic_fields(),
    "christmas": [
        *NAME_FIELDS, f_email(), f_tel(),
        f_text("address", "Address", required=False),
        f_date(),
        f_select("guests", "Estimated Guests", GUESTS_OPTIONS),
        f_select("budget", "Budget Range", BUDGET_OPTIONS),
        f_select("catering", "Catering Selection", CATERING_OPTIONS + ["Turkey or Gigot"]),
        f_checkboxes("entertainment", "Entertainment", ENTERTAINMENT_CHRISTMAS),
        f_checkboxes("decoration", "Chocolate & Decoration", DECOR_CHRISTMAS),
        f_textarea("notes", "Special Instructions for Santa Claus"),
    ],
}

JOIN_US_FIELDS = [
    *NAME_FIELDS, f_email(), f_tel(),
    f_select("position", "Position You're Applying For", ["Performer (Dancer, Musician, Singer)", "Event Coordinator", "Setup Crew", "Costume Designer", "Entertainment Manager", "Other"]),
    f_select("availability", "Availability", ["Weekdays", "Weekends", "Full-Time", "Part-Time", "Freelance"]),
    f_radio("experience_years", "Years Of Experience", ["Beginner", "1 - 3 Years", "3 - 5 Years", "5+ Years", "No experience, but passionate to learn"]),
    f_checkboxes("instruments", "Instrument You Play (if applicable)", ["Trumpet", "Saxophone", "Trombone", "Tuba", "Clarinet", "Clairon", "Darbuka", "Tabl", "Bass Drum", "Snare Drum", "Mizmar", "Mejwiz", "Other"], required=False),
    f_textarea("experience", "Tell Us About Your Experience"),
    f_textarea("why_join", "Why Do You Want To Join Paradream?", required=False),
    f_select("heard_about", "Where Did You Hear About Us", HEAR_ABOUT_OPTIONS, required=False),
    {"kind": "file", "name": "portfolio", "label": "Attach Your Portfolio / Resume", "required": False},
]

CONTACT_FIELDS = [
    *NAME_FIELDS, f_email(), f_tel(),
    f_select("occasion", "Occasion", [label for _, label, _ in OCCASIONS] + ["Other"]),
    f_textarea("message", "Your Message"),
]

# ---------------------------------------------------------------------------
# Form rendering (Netlify Forms: static detection via data-netlify + hidden
# form-name field, so submissions work with zero backend code once deployed)

def render_field(f):
    kind = f["kind"]
    name = f["name"]
    label = f["label"]
    req = "required" if f.get("required") else ""
    if kind in ("text", "email", "tel", "date"):
        itype = {"text": "text", "email": "email", "tel": "tel", "date": "date"}[kind]
        return f"""<label class="field"><span>{label}{' *' if f.get('required') else ''}</span>
        <input type="{itype}" name="{name}" {req}></label>"""
    if kind == "textarea":
        return f"""<label class="field field-wide"><span>{label}{' *' if f.get('required') else ''}</span>
        <textarea name="{name}" rows="4" {req}></textarea></label>"""
    if kind == "select":
        opts = "".join(f'<option value="{o}">{o}</option>' for o in f["options"])
        return f"""<label class="field"><span>{label}{' *' if f.get('required') else ''}</span>
        <select name="{name}" {req}><option value="" disabled selected>Choose...</option>{opts}</select></label>"""
    if kind == "radio":
        opts = "".join(
            f'<label class="choice"><input type="radio" name="{name}" value="{o}" {"required" if f.get("required") else ""}> {o}</label>'
            for o in f["options"]
        )
        return f'<fieldset class="field field-wide"><legend>{label}{" *" if f.get("required") else ""}</legend><div class="choice-group">{opts}</div></fieldset>'
    if kind == "checkboxes":
        opts = "".join(
            f'<label class="choice"><input type="checkbox" name="{name}[]" value="{o}"> {o}</label>'
            for o in f["options"]
        )
        return f'<fieldset class="field field-wide"><legend>{label}</legend><div class="choice-group">{opts}</div></fieldset>'
    if kind == "file":
        return f"""<label class="field field-wide"><span>{label}</span>
        <input type="file" name="{name}"></label>"""
    return ""

def render_form(form_name, fields, submit_label="Submit Request"):
    fields_html = "\n".join(render_field(f) for f in fields)
    return f"""<form class="booking-form" name="{form_name}" method="POST" data-netlify="true" netlify-honeypot="bot-field" enctype="multipart/form-data">
  <input type="hidden" name="form-name" value="{form_name}">
  <p class="hidden-field"><label>Don't fill this out: <input name="bot-field"></label></p>
  <div class="form-grid">
  {fields_html}
  </div>
  <button type="submit" class="btn btn-primary btn-lg">{submit_label}</button>
  <p class="form-note">We'll review your submission and get back to you within 24 to 48 hours. For urgent requests, call or WhatsApp us at <a href="{PHONE_HREF}">{PHONE}</a>.</p>
</form>"""

def hero(kicker, title, subtitle="", cta=None, bg_id="314845_494302"):
    cta_html = f'<a class="btn btn-primary btn-lg" href="{cta[1]}">{cta[0]}</a>' if cta else ""
    bg = find_img(bg_id)
    return f"""<section class="hero" style="background-image:linear-gradient(180deg, rgba(13,13,13,.55), rgba(13,13,13,.75)), url(/assets/img/{bg})">
  <div class="wrap hero-inner">
    {f'<p class="kicker">{kicker}</p>' if kicker else ''}
    <h1>{title}</h1>
    {f'<p class="hero-sub">{subtitle}</p>' if subtitle else ''}
    {cta_html}
  </div>
</section>"""

def gallery_grid(ids, cols="grid-4"):
    tiles = "".join(
        f'<a class="gallery-tile" href="{BASE}/assets/img/{find_img(i)}" data-lightbox>{img(find_img(i), "Paradream Events", "gallery-img")}</a>'
        for i in ids
    )
    return f'<div class="gallery-grid {cols}">{tiles}</div>'

# ---------------------------------------------------------------------------
# Individual pages

def build_home():
    body = hero(
        TAGLINE, "Book Your Dream Event Now!",
        "Your Dream Event Is One Click Away!",
        cta=("Book Now!", f"{BASE}/contact-us.html"),
        bg_id="314845_494302",
    )
    body += f"""
<section class="section section-alt">
  <div class="wrap two-col">
    <div>
      <h2>Discover Our Services</h2>
      <p>Dive into Paradream's portfolio to know what your event will look like.</p>
      <a class="btn btn-outline" href="{BASE}/our-services.html">Our Services</a>
    </div>
    <div>{img(find_img('298930_747690'), 'Paradream event setup', 'rounded-img')}</div>
  </div>
</section>

<section class="section">
  <div class="wrap two-col reverse">
    <div>
      <h2>Join the Paradream Family</h2>
      <p>Be a part of the magic. Join the Paradream family and bring unforgettable moments to life.</p>
      <a class="btn btn-primary" href="{BASE}/join-us.html">Join Now</a>
    </div>
    <div>{img(find_img('197854_416907'), 'Paradream team', 'rounded-img')}</div>
  </div>
</section>

<section class="section section-dark">
  <div class="wrap narrow center">
    <h2>About Us</h2>
    <p>At Paradream Events, we're passionate about turning your most precious moments into unforgettable memories. Based in Beirut, Lebanon, with over 12 years of experience in events, hospitality, and F&amp;B services, our team of dedicated planners handles every detail — from the first consultation to the final applause. Whether it's an intimate baptism or a grand wedding celebration, we bring creativity, professionalism, and heart to every event. You dream it. We achieve it.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2 class="center">How It Works</h2>
    <div class="steps">
      <div class="step"><span class="step-num">1</span><h3>Go to Why Paradream?</h3><p>Choose the Contact Us section to fill in your information.</p></div>
      <div class="step"><span class="step-num">2</span><h3>Fill in The Form</h3><p>Complete the form with all the required information. This will facilitate our ability to process your request effectively and get back to you ASAP!</p></div>
      <div class="step"><span class="step-num">3</span><h3>Trust the Process</h3><p>Trust the process and the planner's workflow to ensure every aspect of the event is managed efficiently and effectively.</p></div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap narrow">
    <h2 class="center">Frequently Asked Questions</h2>
    <div class="faq">
      <details><summary>What is the overall cost of organizing the event, and what factors influence the final price?</summary><p>The overall cost of organizing an event depends on various factors, including the venue, catering, entertainment, staffing, and any additional services or equipment required. The final price is influenced by the size and scope of the event, the complexity of logistics, and the level of customization desired. We provide a detailed estimate based on your specific requirements to ensure transparency and help you manage your budget effectively.</p></details>
      <details><summary>How far in advance should I start planning my event?</summary><p>It is recommended to start planning your event at least 6 to 12 months in advance. This allows enough time for securing venues, arranging vendors, and addressing any logistical details, ensuring a well-organized and successful event. For larger or more complex events, additional planning time may be necessary.</p></details>
      <details><summary>What factors should I consider when setting the event budget?</summary><p>When setting the event budget, the factors to consider will vary based on the type and scale of the event, but the main ones are: venue cost, catering and beverages, entertainment and live shows, theme, table decoration, chocolate, staffing, and more.</p></details>
      <details><summary>Why should I consider hiring an event planner for my upcoming event?</summary><p>Engaging a professional event organizer is essential — their expertise ensures meticulous planning, effective problem-solving, strategic planning, budget management, attention to detail, access to resources, stress reduction, and creative solutions.</p></details>
    </div>
  </div>
</section>
"""
    write("index.html", page(
        "Paradream Events — Lebanon's Trusted Event Planner",
        "Paradream Events — Lebanon's trusted event planning company with 12+ years of experience. We plan weddings, engagements, birthdays, baptisms, Christmas events, and more. Based in Beirut. Contact us today!",
        body, canonical="/",
    ))


def build_why_paradream():
    body = hero("Our Success Story", "Why Paradream?", "How It Started", bg_id="376585_257154")
    body += f"""
<section class="section">
  <div class="wrap narrow center">
    <p>Paradream was established in 2019, with a strong background in hospitality management and event planning. We have a fervent passion for turning dreams into reality. Driven by our love for music and hospitality, and commitment to excellence, we founded Paradream with a clear vision: to make your dreams come true. Our guiding principle, "Your Day, Our Way!", reflects our commitment to bringing your visions to life.</p>
    <p class="stat">200+ celebrations brought to life with unforgettable moments across Lebanon.</p>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <h2 class="center">Here's What Our Clients Say About Paradream</h2>
    <div class="testimonial-grid">
"""
    for (name, quote), iid in zip(TESTIMONIALS, TESTIMONIAL_IMAGES):
        body += f"""      <div class="testimonial-card">
        {img(find_img(iid), name, "testimonial-img")}
        <blockquote>&ldquo;{quote}&rdquo;</blockquote>
        <cite>{name}</cite>
      </div>
"""
    body += """    </div>
    <p class="center"><a class="btn btn-outline" href="https://www.google.com/search?q=Paradream+Events+Lebanon+reviews" target="_blank" rel="noopener">Read Our Google Reviews</a></p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <h2 class="center">What We Do</h2>
    <p class="center subhead">Occasions We Cover — Proposal, Engagement, Bachelor, Pre-Wedding, Wedding, Baptism, First Communion, Gender Reveal, Birthdays...</p>
    <div class="occasion-grid">
"""
    for slug, label, desc in OCCASIONS:
        body += f"""      <div class="occasion-card">
        <h3>{label}</h3>
        <p>{desc}</p>
        <a class="btn btn-primary btn-sm" href="{BASE}/events/{slug}.html">Book Now</a>
      </div>
"""
    body += """    </div>
  </div>
</section>
"""
    write("why-paradream.html", page(
        "Why Paradream? | Top Event Planner & Parade Experts in Lebanon",
        "Discover why Paradream is Lebanon's top event planner. Unique parades, dazzling shows, and unforgettable zaffahs for every special occasion.",
        body, canonical="/why-paradream.html",
    ))


def build_our_services():
    body = hero("What We Offer", "Our Services", bg_id="197854_416907")
    body += '<section class="section"><div class="wrap"><div class="service-grid">'
    for slug, label, iid in PORTFOLIO:
        body += f"""<a class="service-card" href="{BASE}/portfolio/{slug}.html">
      {img(find_img(iid), label, "service-img")}
      <h3>{label}</h3>
    </a>"""
    body += '</div></div></section>'
    write("our-services.html", page(
        "Our Services - Paradream Events",
        "Explore Paradream's full range of event services: oriental zaffahs, live shows, catering, decoration, mascots, photo booths and more.",
        body, canonical="/our-services.html",
    ))


def build_gallery():
    body = hero("Take A Look", "Gallery", bg_id="298930_747690")
    body += f'<section class="section"><div class="wrap">{gallery_grid(GALLERY_IMAGES)}</div></section>'
    body += f'<script src="{BASE}/assets/js/lightbox.js"></script>'
    write("gallery.html", page(
        "Gallery - Paradream Events",
        "Browse photos from Paradream's events across Lebanon — weddings, zaffahs, birthdays, baptisms, and more.",
        body, canonical="/gallery.html",
    ))


def build_contact_us():
    body = hero(None, "Contact Us", "Your Dream Event Is One Message Away.", bg_id="376585_257154")
    body += f"""
<section class="section">
  <div class="wrap two-col">
    <div>{render_form("contact", CONTACT_FIELDS, "Submit")}</div>
    <div class="contact-info">
      <h2>Connect With Us</h2>
      <p>{ADDRESS}</p>
      <p><a href="{PHONE_HREF}">{PHONE}</a></p>
      <p><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <h3>Check Our Latest Updates On Social Media</h3>
      <div class="social-links">
        <a href="{INSTAGRAM}" target="_blank" rel="noopener">Instagram</a>
        <a href="{FACEBOOK}" target="_blank" rel="noopener">Facebook</a>
      </div>
    </div>
  </div>
</section>
"""
    write("contact-us.html", page(
        "Contact Us - Paradream Events",
        "Get in touch with Paradream Events. Your dream event is one message away.",
        body, canonical="/contact-us.html",
    ))


def build_join_us():
    body = hero("Be A Part Of Our Family", "Join Our Team", "Work With Us", bg_id="197854_416907")
    body += f'<section class="section"><div class="wrap narrow">{render_form("join-us", JOIN_US_FIELDS, "Submit Application")}</div></section>'
    write("join-us.html", page(
        "Join Us - Paradream Events",
        "Join the Paradream family. We're always looking for talented performers, coordinators, and creatives to join our team.",
        body, canonical="/join-us.html",
    ))


def build_cookie_policy():
    body = f"""
<section class="section">
  <div class="wrap narrow legal">
    <h1>Cookie Policy</h1>
    <h2>What Are Cookies?</h2>
    <p>Cookies are small pieces of data stored on your computer or device via your browser by sites you visit. As is common practice with almost all websites, this site uses cookies to improve your experience by remembering your preferences and enabling other cookie-based features (e.g. analytics), either for a single visit (through a "session cookie") or for multiple repeat visits (using a "persistent cookie").</p>
    <h2>Our Cookies</h2>
    <p>We use cookies for a number of different purposes, including keeping the site working correctly and understanding how visitors use it.</p>
    <h2>Third-Party Cookies</h2>
    <p>In special cases, we also use cookies provided by trusted third parties like Google Analytics. Third-party analytics are used to track and measure usage of this site so that we can continue to produce engaging content.</p>
    <h2>Managing Cookies</h2>
    <p>When you first access the site, you may receive a message advising you that cookies and similar technologies are in use. By clicking "Accept", you signify that you understand and agree to the use of these technologies, as described in this Cookie Policy.</p>
    <p>You may withdraw consent at any time. Most browsers allow you to refuse to accept cookies, and you can remove cookies from your browser settings. Be aware that disabling cookies may affect the functionality of this and many other websites you visit.</p>
    <p>Please see the following links for information on how to manage, block, or delete cookies for the most popular browsers:</p>
    <ul>
      <li><a href="https://support.microsoft.com/en-us/edge/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use" target="_blank" rel="noopener">Microsoft Edge</a></li>
      <li><a href="https://support.google.com/chrome/answer/95647" target="_blank" rel="noopener">Google Chrome</a></li>
      <li><a href="https://support.mozilla.org/en-US/kb/enable-and-disable-cookies-website-preferences" target="_blank" rel="noopener">Mozilla Firefox</a></li>
      <li><a href="https://support.apple.com/en-gb/guide/safari/sfri11471/mac" target="_blank" rel="noopener">Apple Safari</a></li>
    </ul>
    <h2>General</h2>
    <p>We may edit this policy from time to time. Please check this policy regularly for any changes.</p>
  </div>
</section>
"""
    write("cookie-policy.html", page(
        "Cookie Policy - Paradream Events",
        "Learn about our site's cookie policy, why we use cookies, and how to manage and delete cookies.",
        body, canonical="/cookie-policy.html",
    ))


def build_events():
    for slug, label in EVENTS:
        fields = EVENT_FORMS[slug]
        desc = dict((s, d) for s, l, d in OCCASIONS)[slug]
        body = hero(TAGLINE, label, desc, bg_id="298930_747690")
        body += f'<section class="section"><div class="wrap narrow">{render_form(slug, fields, "Submit Booking Request")}</div></section>'
        write(f"events/{slug}.html", page(
            f"{label} - Paradream Events",
            f"Book your {label.lower()} with Paradream Events. {desc}",
            body, canonical=f"/events/{slug}.html",
        ))


def build_portfolio():
    for slug, label, _ in PORTFOLIO:
        ids = PORTFOLIO_IMAGES[slug]
        body = hero(TAGLINE, label, bg_id=ids[0])
        body += f'<section class="section"><div class="wrap">{gallery_grid(ids)}</div></section>'
        body += f'<section class="section section-alt"><div class="wrap narrow center"><h2>Ready to bring this to your event?</h2><a class="btn btn-primary btn-lg" href="{BASE}/contact-us.html">Book Now</a></div></section>'
        body += f'<script src="{BASE}/assets/js/lightbox.js"></script>'
        write(f"portfolio/{slug}.html", page(
            f"{label} - Paradream Events",
            f"Our highly skilled and professional team is fully equipped to transform your dream occasion into an extraordinary reality with {label}.",
            body, canonical=f"/portfolio/{slug}.html",
        ))


if __name__ == "__main__":
    build_home()
    build_why_paradream()
    build_our_services()
    build_gallery()
    build_contact_us()
    build_join_us()
    build_cookie_policy()
    build_events()
    build_portfolio()
    print("\nDone.")
