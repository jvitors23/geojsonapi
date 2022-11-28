# Generated by Django 4.1.3 on 2022-11-28 01:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Provider",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(blank=True, editable=False, null=True)),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("name", models.CharField(max_length=255)),
                ("phone_number", models.CharField(max_length=20)),
                (
                    "language",
                    models.CharField(
                        choices=[
                            ("ab", "Abkhazian"),
                            ("aa", "Afar"),
                            ("af", "Afrikaans"),
                            ("ak", "Akan"),
                            ("sq", "Albanian"),
                            ("am", "Amharic"),
                            ("ar", "Arabic"),
                            ("an", "Aragonese"),
                            ("hy", "Armenian"),
                            ("as", "Assamese"),
                            ("av", "Avaric"),
                            ("ae", "Avestan"),
                            ("ay", "Aymara"),
                            ("az", "Azerbaijani"),
                            ("bm", "Bambara"),
                            ("ba", "Bashkir"),
                            ("eu", "Basque"),
                            ("be", "Belarusian"),
                            ("bn", "Bengali"),
                            ("bi", "Bislama"),
                            ("bs", "Bosnian"),
                            ("br", "Breton"),
                            ("bg", "Bulgarian"),
                            ("my", "Burmese"),
                            ("ca", "Catalan"),
                            ("km", "Central Khmer"),
                            ("ch", "Chamorro"),
                            ("ce", "Chechen"),
                            ("zh", "Chinese"),
                            ("cu", "Church Slavic"),
                            ("cv", "Chuvash"),
                            ("kw", "Cornish"),
                            ("co", "Corsican"),
                            ("cr", "Cree"),
                            ("hr", "Croatian"),
                            ("cs", "Czech"),
                            ("da", "Danish"),
                            ("dv", "Dhivehi"),
                            ("nl", "Dutch"),
                            ("dz", "Dzongkha"),
                            ("en", "English"),
                            ("eo", "Esperanto"),
                            ("et", "Estonian"),
                            ("ee", "Ewe"),
                            ("fo", "Faroese"),
                            ("fj", "Fijian"),
                            ("fi", "Finnish"),
                            ("fr", "French"),
                            ("ff", "Fulah"),
                            ("gl", "Galician"),
                            ("lg", "Ganda"),
                            ("ka", "Georgian"),
                            ("de", "German"),
                            ("gn", "Guarani"),
                            ("gu", "Gujarati"),
                            ("ht", "Haitian"),
                            ("ha", "Hausa"),
                            ("he", "Hebrew"),
                            ("hz", "Herero"),
                            ("hi", "Hindi"),
                            ("ho", "Hiri Motu"),
                            ("hu", "Hungarian"),
                            ("is", "Icelandic"),
                            ("io", "Ido"),
                            ("ig", "Igbo"),
                            ("id", "Indonesian"),
                            ("ia", "Interlingua (International Auxiliary Language Association)"),
                            ("ie", "Interlingue"),
                            ("iu", "Inuktitut"),
                            ("ik", "Inupiaq"),
                            ("ga", "Irish"),
                            ("it", "Italian"),
                            ("ja", "Japanese"),
                            ("jv", "Javanese"),
                            ("kl", "Kalaallisut"),
                            ("kn", "Kannada"),
                            ("kr", "Kanuri"),
                            ("ks", "Kashmiri"),
                            ("kk", "Kazakh"),
                            ("ki", "Kikuyu"),
                            ("rw", "Kinyarwanda"),
                            ("ky", "Kirghiz"),
                            ("kv", "Komi"),
                            ("kg", "Kongo"),
                            ("ko", "Korean"),
                            ("kj", "Kuanyama"),
                            ("ku", "Kurdish"),
                            ("lo", "Lao"),
                            ("la", "Latin"),
                            ("lv", "Latvian"),
                            ("li", "Limburgan"),
                            ("ln", "Lingala"),
                            ("lt", "Lithuanian"),
                            ("lu", "Luba-Katanga"),
                            ("lb", "Luxembourgish"),
                            ("mk", "Macedonian"),
                            ("mg", "Malagasy"),
                            ("ms", "Malay (macrolanguage)"),
                            ("ml", "Malayalam"),
                            ("mt", "Maltese"),
                            ("gv", "Manx"),
                            ("mi", "Maori"),
                            ("mr", "Marathi"),
                            ("mh", "Marshallese"),
                            ("el", "Modern Greek (1453-)"),
                            ("mn", "Mongolian"),
                            ("na", "Nauru"),
                            ("nv", "Navajo"),
                            ("ng", "Ndonga"),
                            ("ne", "Nepali (macrolanguage)"),
                            ("nd", "North Ndebele"),
                            ("se", "Northern Sami"),
                            ("no", "Norwegian"),
                            ("nb", "Norwegian Bokmål"),
                            ("nn", "Norwegian Nynorsk"),
                            ("ny", "Nyanja"),
                            ("oc", "Occitan (post 1500)"),
                            ("oj", "Ojibwa"),
                            ("or", "Oriya (macrolanguage)"),
                            ("om", "Oromo"),
                            ("os", "Ossetian"),
                            ("pi", "Pali"),
                            ("pa", "Panjabi"),
                            ("fa", "Persian"),
                            ("pl", "Polish"),
                            ("pt", "Portuguese"),
                            ("ps", "Pushto"),
                            ("qu", "Quechua"),
                            ("ro", "Romanian"),
                            ("rm", "Romansh"),
                            ("rn", "Rundi"),
                            ("ru", "Russian"),
                            ("sm", "Samoan"),
                            ("sg", "Sango"),
                            ("sa", "Sanskrit"),
                            ("sc", "Sardinian"),
                            ("gd", "Scottish Gaelic"),
                            ("sr", "Serbian"),
                            ("sh", "Serbo-Croatian"),
                            ("sn", "Shona"),
                            ("ii", "Sichuan Yi"),
                            ("sd", "Sindhi"),
                            ("si", "Sinhala"),
                            ("sk", "Slovak"),
                            ("sl", "Slovenian"),
                            ("so", "Somali"),
                            ("nr", "South Ndebele"),
                            ("st", "Southern Sotho"),
                            ("es", "Spanish"),
                            ("su", "Sundanese"),
                            ("sw", "Swahili (macrolanguage)"),
                            ("ss", "Swati"),
                            ("sv", "Swedish"),
                            ("tl", "Tagalog"),
                            ("ty", "Tahitian"),
                            ("tg", "Tajik"),
                            ("ta", "Tamil"),
                            ("tt", "Tatar"),
                            ("te", "Telugu"),
                            ("th", "Thai"),
                            ("bo", "Tibetan"),
                            ("ti", "Tigrinya"),
                            ("to", "Tonga (Tonga Islands)"),
                            ("ts", "Tsonga"),
                            ("tn", "Tswana"),
                            ("tr", "Turkish"),
                            ("tk", "Turkmen"),
                            ("tw", "Twi"),
                            ("ug", "Uighur"),
                            ("uk", "Ukrainian"),
                            ("ur", "Urdu"),
                            ("uz", "Uzbek"),
                            ("ve", "Venda"),
                            ("vi", "Vietnamese"),
                            ("vo", "Volapük"),
                            ("wa", "Walloon"),
                            ("cy", "Welsh"),
                            ("fy", "Western Frisian"),
                            ("wo", "Wolof"),
                            ("xh", "Xhosa"),
                            ("yi", "Yiddish"),
                            ("yo", "Yoruba"),
                            ("za", "Zhuang"),
                            ("zu", "Zulu"),
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "currency",
                    models.CharField(
                        choices=[
                            ("AED", "AED - UAE Dirham"),
                            ("AFN", "AFN - Afghani"),
                            ("ALL", "ALL - Lek"),
                            ("AMD", "AMD - Armenian Dram"),
                            ("ANG", "ANG - Netherlands Antillean Guilder"),
                            ("AOA", "AOA - Kwanza"),
                            ("ARS", "ARS - Argentine Peso"),
                            ("AUD", "AUD - Australian Dollar"),
                            ("AWG", "AWG - Aruban Florin"),
                            ("AZN", "AZN - Azerbaijanian Manat"),
                            ("BAM", "BAM - Convertible Mark"),
                            ("BBD", "BBD - Barbados Dollar"),
                            ("BDT", "BDT - Taka"),
                            ("BGN", "BGN - Bulgarian Lev"),
                            ("BHD", "BHD - Bahraini Dinar"),
                            ("BIF", "BIF - Burundi Franc"),
                            ("BMD", "BMD - Bermudian Dollar"),
                            ("BND", "BND - Brunei Dollar"),
                            ("BOB", "BOB - Boliviano"),
                            ("BRL", "BRL - Brazilian Real"),
                            ("BSD", "BSD - Bahamian Dollar"),
                            ("BTN", "BTN - Ngultrum"),
                            ("BWP", "BWP - Pula"),
                            ("BYN", "BYN - Belarusian Ruble"),
                            ("BZD", "BZD - Belize Dollar"),
                            ("CAD", "CAD - Canadian Dollar"),
                            ("CDF", "CDF - Congolese Franc"),
                            ("CHF", "CHF - Swiss Franc"),
                            ("CLP", "CLP - Chilean Peso"),
                            ("CNY", "CNY - Yuan Renminbi"),
                            ("COP", "COP - Colombian Peso"),
                            ("CRC", "CRC - Costa Rican Colon"),
                            ("CUC", "CUC - Peso Convertible"),
                            ("CUP", "CUP - Cuban Peso"),
                            ("CVE", "CVE - Cabo Verde Escudo"),
                            ("CZK", "CZK - Czech Koruna"),
                            ("DJF", "DJF - Djibouti Franc"),
                            ("DKK", "DKK - Danish Krone"),
                            ("DOP", "DOP - Dominican Peso"),
                            ("DZD", "DZD - Algerian Dinar"),
                            ("EGP", "EGP - Egyptian Pound"),
                            ("ERN", "ERN - Nakfa"),
                            ("ETB", "ETB - Ethiopian Birr"),
                            ("EUR", "EUR - Euro"),
                            ("FJD", "FJD - Fiji Dollar"),
                            ("FKP", "FKP - Falkland Islands Pound"),
                            ("GBP", "GBP - Pound Sterling"),
                            ("GEL", "GEL - Lari"),
                            ("GHS", "GHS - Ghana Cedi"),
                            ("GIP", "GIP - Gibraltar Pound"),
                            ("GMD", "GMD - Dalasi"),
                            ("GNF", "GNF - Guinea Franc"),
                            ("GTQ", "GTQ - Quetzal"),
                            ("GYD", "GYD - Guyana Dollar"),
                            ("HKD", "HKD - Hong Kong Dollar"),
                            ("HNL", "HNL - Lempira"),
                            ("HRK", "HRK - Kuna"),
                            ("HTG", "HTG - Gourde"),
                            ("HUF", "HUF - Forint"),
                            ("IDR", "IDR - Rupiah"),
                            ("ILS", "ILS - New Israeli Sheqel"),
                            ("INR", "INR - Indian Rupee"),
                            ("IQD", "IQD - Iraqi Dinar"),
                            ("IRR", "IRR - Iranian Rial"),
                            ("ISK", "ISK - Iceland Krona"),
                            ("JMD", "JMD - Jamaican Dollar"),
                            ("JOD", "JOD - Jordanian Dinar"),
                            ("JPY", "JPY - Yen"),
                            ("KES", "KES - Kenyan Shilling"),
                            ("KGS", "KGS - Som"),
                            ("KHR", "KHR - Riel"),
                            ("KMF", "KMF - Comoro Franc"),
                            ("KPW", "KPW - North Korean Won"),
                            ("KRW", "KRW - Won"),
                            ("KWD", "KWD - Kuwaiti Dinar"),
                            ("KYD", "KYD - Cayman Islands Dollar"),
                            ("KZT", "KZT - Tenge"),
                            ("LAK", "LAK - Kip"),
                            ("LBP", "LBP - Lebanese Pound"),
                            ("LKR", "LKR - Sri Lanka Rupee"),
                            ("LRD", "LRD - Liberian Dollar"),
                            ("LSL", "LSL - Loti"),
                            ("LYD", "LYD - Libyan Dinar"),
                            ("MAD", "MAD - Moroccan Dirham"),
                            ("MDL", "MDL - Moldovan Leu"),
                            ("MGA", "MGA - Malagasy Ariary"),
                            ("MKD", "MKD - Denar"),
                            ("MMK", "MMK - Kyat"),
                            ("MNT", "MNT - Tugrik"),
                            ("MOP", "MOP - Pataca"),
                            ("MRO", "MRO - Ouguiya"),
                            ("MUR", "MUR - Mauritius Rupee"),
                            ("MVR", "MVR - Rufiyaa"),
                            ("MWK", "MWK - Malawi Kwacha"),
                            ("MXN", "MXN - Mexican Peso"),
                            ("MYR", "MYR - Malaysian Ringgit"),
                            ("MZN", "MZN - Mozambique Metical"),
                            ("NAD", "NAD - Namibia Dollar"),
                            ("NGN", "NGN - Naira"),
                            ("NIO", "NIO - Cordoba Oro"),
                            ("NOK", "NOK - Norwegian Krone"),
                            ("NPR", "NPR - Nepalese Rupee"),
                            ("NZD", "NZD - New Zealand Dollar"),
                            ("OMR", "OMR - Rial Omani"),
                            ("PAB", "PAB - Balboa"),
                            ("PEN", "PEN - Sol"),
                            ("PGK", "PGK - Kina"),
                            ("PHP", "PHP - Philippine Peso"),
                            ("PKR", "PKR - Pakistan Rupee"),
                            ("PLN", "PLN - Zloty"),
                            ("PYG", "PYG - Guarani"),
                            ("QAR", "QAR - Qatari Rial"),
                            ("RON", "RON - Romanian Leu"),
                            ("RSD", "RSD - Serbian Dinar"),
                            ("RUB", "RUB - Russian Ruble"),
                            ("RWF", "RWF - Rwanda Franc"),
                            ("SAR", "SAR - Saudi Riyal"),
                            ("SBD", "SBD - Solomon Islands Dollar"),
                            ("SCR", "SCR - Seychelles Rupee"),
                            ("SDG", "SDG - Sudanese Pound"),
                            ("SEK", "SEK - Swedish Krona"),
                            ("SGD", "SGD - Singapore Dollar"),
                            ("SHP", "SHP - Saint Helena Pound"),
                            ("SLL", "SLL - Leone"),
                            ("SOS", "SOS - Somali Shilling"),
                            ("SRD", "SRD - Surinam Dollar"),
                            ("SSP", "SSP - South Sudanese Pound"),
                            ("STD", "STD - Dobra"),
                            ("SVC", "SVC - El Salvador Colon"),
                            ("SYP", "SYP - Syrian Pound"),
                            ("SZL", "SZL - Lilangeni"),
                            ("THB", "THB - Baht"),
                            ("TJS", "TJS - Somoni"),
                            ("TMT", "TMT - Turkmenistan New Manat"),
                            ("TND", "TND - Tunisian Dinar"),
                            ("TOP", "TOP - Pa’anga"),
                            ("TRY", "TRY - Turkish Lira"),
                            ("TTD", "TTD - Trinidad and Tobago Dollar"),
                            ("TWD", "TWD - New Taiwan Dollar"),
                            ("TZS", "TZS - Tanzanian Shilling"),
                            ("UAH", "UAH - Hryvnia"),
                            ("UGX", "UGX - Uganda Shilling"),
                            ("USD", "USD - US Dollar"),
                            ("UYU", "UYU - Peso Uruguayo"),
                            ("UZS", "UZS - Uzbekistan Sum"),
                            ("VEF", "VEF - Bolívar"),
                            ("VND", "VND - Dong"),
                            ("VUV", "VUV - Vatu"),
                            ("WST", "WST - Tala"),
                            ("XAF", "XAF - CFA Franc BEAC"),
                            ("XAG", "XAG - Silver"),
                            ("XAU", "XAU - Gold"),
                            ("XBA", "XBA - Bond Markets Unit European Composite Unit (EURCO)"),
                            ("XBB", "XBB - Bond Markets Unit European Monetary Unit (E.M.U.-6)"),
                            ("XBC", "XBC - Bond Markets Unit European Unit of Account 9 (E.U.A.-9)"),
                            ("XBD", "XBD - Bond Markets Unit European Unit of Account 17 (E.U.A.-17)"),
                            ("XCD", "XCD - East Caribbean Dollar"),
                            ("XDR", "XDR - SDR (Special Drawing Right)"),
                            ("XOF", "XOF - CFA Franc BCEAO"),
                            ("XPD", "XPD - Palladium"),
                            ("XPF", "XPF - CFP Franc"),
                            ("XPT", "XPT - Platinum"),
                            ("XSU", "XSU - Sucre"),
                            ("XTS", "XTS - Codes specifically reserved for testing purposes"),
                            ("XUA", "XUA - ADB Unit of Account"),
                            ("XXX", "XXX - The codes assigned for transactions where no currency is involved"),
                            ("YER", "YER - Yemeni Rial"),
                            ("ZAR", "ZAR - Rand"),
                            ("ZMW", "ZMW - Zambian Kwacha"),
                            ("ZWL", "ZWL - Zimbabwe Dollar"),
                        ],
                        max_length=3,
                    ),
                ),
                ("owner", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
