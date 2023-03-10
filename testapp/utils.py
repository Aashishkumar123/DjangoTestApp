from django.core.validators import RegexValidator


phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$', 
    message = "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )


CURRENCY_LIST = [
"USD",
"CAD",
"EUR",
"AED",
"AFN",
"ALL",
"AMD",
"ARS",
"AUD",
"AZN",
"BAM",
"BDT",
"BGN",
"BHD",
"BIF",
"BND",
"BOB",
"BRL",
"BWP",
"BYN",
"BZD",
"CDF",
"CHF",
"CLP",
"CNY",
"COP",
"CRC",
"CVE",
"CZK",
"DJF",
"DKK",
"DOP",
"DZD",
"EEK",
"EGP",
"ERN",
"ETB",
"GBP",
"GEL",
"GHS",
"GNF",
"GTQ",
"HKD",
"HNL",
"HRK",
"HUF",
"IDR",
"ILS",
"INR",
"IQD",
"IRR",
"ISK",
"JMD",
"JOD",
"JPY",
"KES",
"KHR",
"KMF",
"KRW",
"KWD",
"KZT",
"LBP",
"LKRs",
"LTL",
"LVL",
"LYD",
"MAD",
"MDL",
"MGA",
"MKD",
"MMK",
"MOP",
"MURs",
"MXN",
"MYR",
"MZN",
"NAD",
"NGN",
"NIO",
"NOK",
"NPRs",
"NZD",
"OMR",
"PAB",
"PEN",
"PHP",
"PKRs",
"PLN",
"PYG",
"QAR",
"RON",
"RSD",
"RUB",
"RWF",
"SAR",
"SDG",
"SEK",
"SGD",
"SOS",
"SYP",
"THB",
"TND",
"TOP",
"TRY",
"TTD",
"TWD",
"TZS",
"UAH",
"UGX",
"UYU",
"UZS",
"VEFF",
"VND",
"XAFA",
"XOF",
"YER",
"ZAR",
"ZMK",
"ZWL",
]


COUNTRY_LIST = [ 
'Afghanistan', 
'Åland Islands', 
'Albania', 
'Algeria', 
'American Samoa', 
'AndorrA', 
'Angola', 
'Anguilla', 
'Antarctica', 
'Antigua and Barbuda', 
'Argentina', 
'Armenia', 
'Aruba', 
'Australia', 
'Austria', 
'Azerbaijan', 
'Bahamas', 
'Bahrain', 
'Bangladesh', 
'Barbados', 
'Belarus', 
'Belgium', 
'Belize', 
'Benin', 
'Bermuda', 
'Bhutan', 
'Bolivia', 
'Bosnia and Herzegovina', 
'Botswana', 
'Bouvet Island', 
'Brazil', 
'British Indian Ocean Territory', 
'Brunei Darussalam', 
'Bulgaria', 
'Burkina Faso', 
'Burundi', 
'Cambodia', 
'Cameroon', 
'Canada', 
'Cape Verde', 
'Cayman Islands', 
'Central African Republic', 
'Chad', 
'Chile', 
'China', 
'Christmas Island', 
'Cocos (Keeling) Islands', 
'Colombia', 
'Comoros', 
'Congo', 
'Congo, The Democratic Republic of the', 
'Cook Islands', 
'Costa Rica', 
'Cote D\'Ivoire', 
'Croatia', 
'Cuba', 
'Cyprus', 
'Czech Republic', 
'Denmark', 
'Djibouti', 
'Dominica', 
'Dominican Republic', 
'Ecuador', 
'Egypt', 
'El Salvador', 
'Equatorial Guinea', 
'Eritrea', 
'Estonia', 
'Ethiopia', 
'Falkland Islands (Malvinas)', 
'Faroe Islands', 
'Fiji', 
'Finland', 
'France', 
'French Guiana', 
'French Polynesia', 
'French Southern Territories', 
'Gabon', 
'Gambia', 
'Georgia', 
'Germany', 
'Ghana', 
'Gibraltar', 
'Greece', 
'Greenland', 
'Grenada', 
'Guadeloupe', 
'Guam', 
'Guatemala', 
'Guernsey', 
'Guinea', 
'Guinea-Bissau', 
'Guyana', 
'Haiti', 
'Heard Island and Mcdonald Islands', 
'Holy See (Vatican City State)', 
'Honduras', 
'Hong Kong', 
'Hungary', 
'Iceland', 
'India', 
'Indonesia', 
'Iran, Islamic Republic Of', 
'Iraq', 
'Ireland', 
'Isle of Man', 
'Israel', 
'Italy', 
'Jamaica', 
'Japan', 
'Jersey', 
'Jordan', 
'Kazakhstan', 
'Kenya', 
'Kiribati', 
'Korea, Democratic People\'S Republic of', 
'Korea, Republic of', 
'Kuwait', 
'Kyrgyzstan', 
'Lao People\'S Democratic Republic', 
'Latvia', 
'Lebanon', 
'Lesotho', 
'Liberia', 
'Libyan Arab Jamahiriya', 
'Liechtenstein', 
'Lithuania', 
'Luxembourg', 
'Macao', 
'Macedonia, The Former Yugoslav Republic of', 
'Madagascar', 
'Malawi', 
'Malaysia', 
'Maldives', 
'Mali', 
'Malta', 
'Marshall Islands', 
'Martinique', 
'Mauritania', 
'Mauritius', 
'Mayotte', 
'Mexico', 
'Micronesia, Federated States of', 
'Moldova, Republic of', 
'Monaco', 
'Mongolia', 
'Montserrat', 
'Morocco', 
'Mozambique', 
'Myanmar', 
'Namibia', 
'Nauru', 
'Nepal', 
'Netherlands', 
'Netherlands Antilles', 
'New Caledonia', 
'New Zealand', 
'Nicaragua', 
'Niger', 
'Nigeria', 
'Niue', 
'Norfolk Island', 
'Northern Mariana Islands', 
'Norway', 
'Oman', 
'Pakistan', 
'Palau', 
'Palestinian Territory, Occupied', 
'Panama', 
'Papua New Guinea', 
'Paraguay', 
'Peru', 
'Philippines', 
'Pitcairn', 
'Poland', 
'Portugal', 
'Puerto Rico', 
'Qatar', 
'Reunion', 
'Romania', 
'Russian Federation', 
'RWANDA', 
'Saint Helena', 
'Saint Kitts and Nevis', 
'Saint Lucia', 
'Saint Pierre and Miquelon', 
'Saint Vincent and the Grenadines', 
'Samoa', 
'San Marino', 
'Sao Tome and Principe', 
'Saudi Arabia', 
'Senegal', 
'Serbia and Montenegro', 
'Seychelles', 
'Sierra Leone', 
'Singapore', 
'Slovakia', 
'Slovenia', 
'Solomon Islands', 
'Somalia', 
'South Africa', 
'South Georgia and the South Sandwich Islands', 
'Spain', 
'Sri Lanka', 
'Sudan', 
'Suriname', 
'Svalbard and Jan Mayen', 
'Swaziland', 
'Sweden', 
'Switzerland', 
'Syrian Arab Republic', 
'Taiwan, Province of China', 
'Tajikistan', 
'Tanzania, United Republic of', 
'Thailand', 
'Timor-Leste', 
'Togo', 
'Tokelau', 
'Tonga', 
'Trinidad and Tobago', 
'Tunisia', 
'Turkey', 
'Turkmenistan', 
'Turks and Caicos Islands', 
'Tuvalu', 
'Uganda', 
'Ukraine', 
'United Arab Emirates', 
'United Kingdom', 
'United States', 
'United States Minor Outlying Islands', 
'Uruguay', 
'Uzbekistan', 
'Vanuatu', 
'Venezuela', 
'Viet Nam', 
'Virgin Islands, British', 
'Virgin Islands, U.S.', 
'Wallis and Futuna', 
'Western Sahara', 
'Yemen', 
'Zambia', 
'Zimbabwe' 
]
