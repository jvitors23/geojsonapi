# Generated by Django 4.1.3 on 2022-11-27 19:25

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
                            ("aa", "Afar"),
                            ("ab", "Abkhazian"),
                            ("af", "Afrikaans"),
                            ("ak", "Akan"),
                            ("am", "Amharic"),
                            ("ar", "Arabic"),
                            ("an", "Aragonese"),
                            ("as", "Assamese"),
                            ("av", "Avaric"),
                            ("ae", "Avestan"),
                            ("ay", "Aymara"),
                            ("az", "Azerbaijani"),
                            ("ba", "Bashkir"),
                            ("bm", "Bambara"),
                            ("be", "Belarusian"),
                            ("bn", "Bengali"),
                            ("bi", "Bislama"),
                            ("bo", "Tibetan"),
                            ("bs", "Bosnian"),
                            ("br", "Breton"),
                            ("bg", "Bulgarian"),
                            ("ca", "Catalan"),
                            ("cs", "Czech"),
                            ("ch", "Chamorro"),
                            ("ce", "Chechen"),
                            ("cu", "Church Slavic"),
                            ("cv", "Chuvash"),
                            ("kw", "Cornish"),
                            ("co", "Corsican"),
                            ("cr", "Cree"),
                            ("cy", "Welsh"),
                            ("da", "Danish"),
                            ("de", "German"),
                            ("dv", "Dhivehi"),
                            ("dz", "Dzongkha"),
                            ("el", "Modern Greek (1453-)"),
                            ("en", "English"),
                            ("eo", "Esperanto"),
                            ("et", "Estonian"),
                            ("eu", "Basque"),
                            ("ee", "Ewe"),
                            ("fo", "Faroese"),
                            ("fa", "Persian"),
                            ("fj", "Fijian"),
                            ("fi", "Finnish"),
                            ("fr", "French"),
                            ("fy", "Western Frisian"),
                            ("ff", "Fulah"),
                            ("gd", "Scottish Gaelic"),
                            ("ga", "Irish"),
                            ("gl", "Galician"),
                            ("gv", "Manx"),
                            ("gn", "Guarani"),
                            ("gu", "Gujarati"),
                            ("ht", "Haitian"),
                            ("ha", "Hausa"),
                            ("sh", "Serbo-Croatian"),
                            ("he", "Hebrew"),
                            ("hz", "Herero"),
                            ("hi", "Hindi"),
                            ("ho", "Hiri Motu"),
                            ("hr", "Croatian"),
                            ("hu", "Hungarian"),
                            ("hy", "Armenian"),
                            ("ig", "Igbo"),
                            ("io", "Ido"),
                            ("ii", "Sichuan Yi"),
                            ("iu", "Inuktitut"),
                            ("ie", "Interlingue"),
                            ("ia", "Interlingua (International Auxiliary Language Association)"),
                            ("id", "Indonesian"),
                            ("ik", "Inupiaq"),
                            ("is", "Icelandic"),
                            ("it", "Italian"),
                            ("jv", "Javanese"),
                            ("ja", "Japanese"),
                            ("kl", "Kalaallisut"),
                            ("kn", "Kannada"),
                            ("ks", "Kashmiri"),
                            ("ka", "Georgian"),
                            ("kr", "Kanuri"),
                            ("kk", "Kazakh"),
                            ("km", "Central Khmer"),
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
                            ("lb", "Luxembourgish"),
                            ("lu", "Luba-Katanga"),
                            ("lg", "Ganda"),
                            ("mh", "Marshallese"),
                            ("ml", "Malayalam"),
                            ("mr", "Marathi"),
                            ("mk", "Macedonian"),
                            ("mg", "Malagasy"),
                            ("mt", "Maltese"),
                            ("mn", "Mongolian"),
                            ("mi", "Maori"),
                            ("ms", "Malay (macrolanguage)"),
                            ("my", "Burmese"),
                            ("na", "Nauru"),
                            ("nv", "Navajo"),
                            ("nr", "South Ndebele"),
                            ("nd", "North Ndebele"),
                            ("ng", "Ndonga"),
                            ("ne", "Nepali (macrolanguage)"),
                            ("nl", "Dutch"),
                            ("nn", "Norwegian Nynorsk"),
                            ("nb", "Norwegian Bokmål"),
                            ("no", "Norwegian"),
                            ("ny", "Nyanja"),
                            ("oc", "Occitan (post 1500)"),
                            ("oj", "Ojibwa"),
                            ("or", "Oriya (macrolanguage)"),
                            ("om", "Oromo"),
                            ("os", "Ossetian"),
                            ("pa", "Panjabi"),
                            ("pi", "Pali"),
                            ("pl", "Polish"),
                            ("pt", "Portuguese"),
                            ("ps", "Pushto"),
                            ("qu", "Quechua"),
                            ("rm", "Romansh"),
                            ("ro", "Romanian"),
                            ("rn", "Rundi"),
                            ("ru", "Russian"),
                            ("sg", "Sango"),
                            ("sa", "Sanskrit"),
                            ("si", "Sinhala"),
                            ("sk", "Slovak"),
                            ("sl", "Slovenian"),
                            ("se", "Northern Sami"),
                            ("sm", "Samoan"),
                            ("sn", "Shona"),
                            ("sd", "Sindhi"),
                            ("so", "Somali"),
                            ("st", "Southern Sotho"),
                            ("es", "Spanish"),
                            ("sq", "Albanian"),
                            ("sc", "Sardinian"),
                            ("sr", "Serbian"),
                            ("ss", "Swati"),
                            ("su", "Sundanese"),
                            ("sw", "Swahili (macrolanguage)"),
                            ("sv", "Swedish"),
                            ("ty", "Tahitian"),
                            ("ta", "Tamil"),
                            ("tt", "Tatar"),
                            ("te", "Telugu"),
                            ("tg", "Tajik"),
                            ("tl", "Tagalog"),
                            ("th", "Thai"),
                            ("ti", "Tigrinya"),
                            ("to", "Tonga (Tonga Islands)"),
                            ("tn", "Tswana"),
                            ("ts", "Tsonga"),
                            ("tk", "Turkmen"),
                            ("tr", "Turkish"),
                            ("tw", "Twi"),
                            ("ug", "Uighur"),
                            ("uk", "Ukrainian"),
                            ("ur", "Urdu"),
                            ("uz", "Uzbek"),
                            ("ve", "Venda"),
                            ("vi", "Vietnamese"),
                            ("vo", "Volapük"),
                            ("wa", "Walloon"),
                            ("wo", "Wolof"),
                            ("xh", "Xhosa"),
                            ("yi", "Yiddish"),
                            ("yo", "Yoruba"),
                            ("za", "Zhuang"),
                            ("zh", "Chinese"),
                            ("zu", "Zulu"),
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "currency",
                    models.CharField(
                        choices=[
                            ("AED", "UAE Dirham"),
                            ("AFN", "Afghani"),
                            ("ALL", "Lek"),
                            ("AMD", "Armenian Dram"),
                            ("ANG", "Netherlands Antillean Guilder"),
                            ("AOA", "Kwanza"),
                            ("ARS", "Argentine Peso"),
                            ("AUD", "Australian Dollar"),
                            ("AWG", "Aruban Florin"),
                            ("AZN", "Azerbaijanian Manat"),
                            ("BAM", "Convertible Mark"),
                            ("BBD", "Barbados Dollar"),
                            ("BDT", "Taka"),
                            ("BGN", "Bulgarian Lev"),
                            ("BHD", "Bahraini Dinar"),
                            ("BIF", "Burundi Franc"),
                            ("BMD", "Bermudian Dollar"),
                            ("BND", "Brunei Dollar"),
                            ("BOB", "Boliviano"),
                            ("BRL", "Brazilian Real"),
                            ("BSD", "Bahamian Dollar"),
                            ("BTN", "Ngultrum"),
                            ("BWP", "Pula"),
                            ("BYN", "Belarusian Ruble"),
                            ("BZD", "Belize Dollar"),
                            ("CAD", "Canadian Dollar"),
                            ("CDF", "Congolese Franc"),
                            ("CHF", "Swiss Franc"),
                            ("CLP", "Chilean Peso"),
                            ("CNY", "Yuan Renminbi"),
                            ("COP", "Colombian Peso"),
                            ("CRC", "Costa Rican Colon"),
                            ("CUC", "Peso Convertible"),
                            ("CUP", "Cuban Peso"),
                            ("CVE", "Cabo Verde Escudo"),
                            ("CZK", "Czech Koruna"),
                            ("DJF", "Djibouti Franc"),
                            ("DKK", "Danish Krone"),
                            ("DOP", "Dominican Peso"),
                            ("DZD", "Algerian Dinar"),
                            ("EGP", "Egyptian Pound"),
                            ("ERN", "Nakfa"),
                            ("ETB", "Ethiopian Birr"),
                            ("EUR", "Euro"),
                            ("FJD", "Fiji Dollar"),
                            ("FKP", "Falkland Islands Pound"),
                            ("GBP", "Pound Sterling"),
                            ("GEL", "Lari"),
                            ("GHS", "Ghana Cedi"),
                            ("GIP", "Gibraltar Pound"),
                            ("GMD", "Dalasi"),
                            ("GNF", "Guinea Franc"),
                            ("GTQ", "Quetzal"),
                            ("GYD", "Guyana Dollar"),
                            ("HKD", "Hong Kong Dollar"),
                            ("HNL", "Lempira"),
                            ("HRK", "Kuna"),
                            ("HTG", "Gourde"),
                            ("HUF", "Forint"),
                            ("IDR", "Rupiah"),
                            ("ILS", "New Israeli Sheqel"),
                            ("INR", "Indian Rupee"),
                            ("IQD", "Iraqi Dinar"),
                            ("IRR", "Iranian Rial"),
                            ("ISK", "Iceland Krona"),
                            ("JMD", "Jamaican Dollar"),
                            ("JOD", "Jordanian Dinar"),
                            ("JPY", "Yen"),
                            ("KES", "Kenyan Shilling"),
                            ("KGS", "Som"),
                            ("KHR", "Riel"),
                            ("KMF", "Comoro Franc"),
                            ("KPW", "North Korean Won"),
                            ("KRW", "Won"),
                            ("KWD", "Kuwaiti Dinar"),
                            ("KYD", "Cayman Islands Dollar"),
                            ("KZT", "Tenge"),
                            ("LAK", "Kip"),
                            ("LBP", "Lebanese Pound"),
                            ("LKR", "Sri Lanka Rupee"),
                            ("LRD", "Liberian Dollar"),
                            ("LSL", "Loti"),
                            ("LYD", "Libyan Dinar"),
                            ("MAD", "Moroccan Dirham"),
                            ("MDL", "Moldovan Leu"),
                            ("MGA", "Malagasy Ariary"),
                            ("MKD", "Denar"),
                            ("MMK", "Kyat"),
                            ("MNT", "Tugrik"),
                            ("MOP", "Pataca"),
                            ("MRO", "Ouguiya"),
                            ("MUR", "Mauritius Rupee"),
                            ("MVR", "Rufiyaa"),
                            ("MWK", "Malawi Kwacha"),
                            ("MXN", "Mexican Peso"),
                            ("MYR", "Malaysian Ringgit"),
                            ("MZN", "Mozambique Metical"),
                            ("NAD", "Namibia Dollar"),
                            ("NGN", "Naira"),
                            ("NIO", "Cordoba Oro"),
                            ("NOK", "Norwegian Krone"),
                            ("NPR", "Nepalese Rupee"),
                            ("NZD", "New Zealand Dollar"),
                            ("OMR", "Rial Omani"),
                            ("PAB", "Balboa"),
                            ("PEN", "Sol"),
                            ("PGK", "Kina"),
                            ("PHP", "Philippine Peso"),
                            ("PKR", "Pakistan Rupee"),
                            ("PLN", "Zloty"),
                            ("PYG", "Guarani"),
                            ("QAR", "Qatari Rial"),
                            ("RON", "Romanian Leu"),
                            ("RSD", "Serbian Dinar"),
                            ("RUB", "Russian Ruble"),
                            ("RWF", "Rwanda Franc"),
                            ("SAR", "Saudi Riyal"),
                            ("SBD", "Solomon Islands Dollar"),
                            ("SCR", "Seychelles Rupee"),
                            ("SDG", "Sudanese Pound"),
                            ("SEK", "Swedish Krona"),
                            ("SGD", "Singapore Dollar"),
                            ("SHP", "Saint Helena Pound"),
                            ("SLL", "Leone"),
                            ("SOS", "Somali Shilling"),
                            ("SRD", "Surinam Dollar"),
                            ("SSP", "South Sudanese Pound"),
                            ("STD", "Dobra"),
                            ("SVC", "El Salvador Colon"),
                            ("SYP", "Syrian Pound"),
                            ("SZL", "Lilangeni"),
                            ("THB", "Baht"),
                            ("TJS", "Somoni"),
                            ("TMT", "Turkmenistan New Manat"),
                            ("TND", "Tunisian Dinar"),
                            ("TOP", "Pa’anga"),
                            ("TRY", "Turkish Lira"),
                            ("TTD", "Trinidad and Tobago Dollar"),
                            ("TWD", "New Taiwan Dollar"),
                            ("TZS", "Tanzanian Shilling"),
                            ("UAH", "Hryvnia"),
                            ("UGX", "Uganda Shilling"),
                            ("USD", "US Dollar"),
                            ("UYU", "Peso Uruguayo"),
                            ("UZS", "Uzbekistan Sum"),
                            ("VEF", "Bolívar"),
                            ("VND", "Dong"),
                            ("VUV", "Vatu"),
                            ("WST", "Tala"),
                            ("XAF", "CFA Franc BEAC"),
                            ("XAG", "Silver"),
                            ("XAU", "Gold"),
                            ("XBA", "Bond Markets Unit European Composite Unit (EURCO)"),
                            ("XBB", "Bond Markets Unit European Monetary Unit (E.M.U.-6)"),
                            ("XBC", "Bond Markets Unit European Unit of Account 9 (E.U.A.-9)"),
                            ("XBD", "Bond Markets Unit European Unit of Account 17 (E.U.A.-17)"),
                            ("XCD", "East Caribbean Dollar"),
                            ("XDR", "SDR (Special Drawing Right)"),
                            ("XOF", "CFA Franc BCEAO"),
                            ("XPD", "Palladium"),
                            ("XPF", "CFP Franc"),
                            ("XPT", "Platinum"),
                            ("XSU", "Sucre"),
                            ("XTS", "Codes specifically reserved for testing purposes"),
                            ("XUA", "ADB Unit of Account"),
                            ("XXX", "The codes assigned for transactions where no currency is involved"),
                            ("YER", "Yemeni Rial"),
                            ("ZAR", "Rand"),
                            ("ZMW", "Zambian Kwacha"),
                            ("ZWL", "Zimbabwe Dollar"),
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
