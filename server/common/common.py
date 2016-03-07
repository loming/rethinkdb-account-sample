from singleton import Singleton

class Constant(Singleton):
    COUNTRY_LIST = [
        {'short': "  ", 'name': "Please select a country"},
        {'short': "AF", 'name': "Afghanistan"},
        {'short': "AL", 'name': "Albania"},
        {'short': "DZ", 'name': "Algeria"},
        {'short': "AS", 'name': "American Samoa"},
        {'short': "AD", 'name': "Andorra"},
        {'short': "AO", 'name': "Angola"},
        {'short': "AI", 'name': "Anguilla"},
        {'short': "AQ", 'name': "Antarctica"},
        {'short': "AG", 'name': "Antigua and Barbuda"},
        {'short': "AR", 'name': "Argentina"},
        {'short': "AM", 'name': "Armenia"},
        {'short': "AW", 'name': "Aruba"},
        {'short': "AU", 'name': "Australia"},
        {'short': "AT", 'name': "Austria"},
        {'short': "AZ", 'name': "Azerbaijan"},
        {'short': "BS", 'name': "Bahamas"},
        {'short': "BH", 'name': "Bahrain"},
        {'short': "BD", 'name': "Bangladesh"},
        {'short': "BB", 'name': "Barbados"},
        {'short': "BY", 'name': "Belarus"},
        {'short': "BE", 'name': "Belgium"},
        {'short': "BZ", 'name': "Belize"},
        {'short': "BJ", 'name': "Benin"},
        {'short': "BM", 'name': "Bermuda"},
        {'short': "BT", 'name': "Bhutan"},
        {'short': "BO", 'name': "Bolivia"},
        {'short': "BA", 'name': "Bosnia and Herzegowina"},
        {'short': "BW", 'name': "Botswana"},
        {'short': "BV", 'name': "Bouvet Island"},
        {'short': "BR", 'name': "Brazil"},
        {'short': "IO", 'name': "British Indian Ocean Territory"},
        {'short': "BN", 'name': "Brunei Darussalam"},
        {'short': "BG", 'name': "Bulgaria"},
        {'short': "BF", 'name': "Burkina Faso"},
        {'short': "BI", 'name': "Burundi"},
        {'short': "KH", 'name': "Cambodia"},
        {'short': "CM", 'name': "Cameroon"},
        {'short': "CA", 'name': "Canada"},
        {'short': "CV", 'name': "Cape Verde"},
        {'short': "KY", 'name': "Cayman Islands"},
        {'short': "CF", 'name': "Central African Republic"},
        {'short': "TD", 'name': "Chad"},
        {'short': "CL", 'name': "Chile"},
        {'short': "CN", 'name': "China"},
        {'short': "CX", 'name': "Christmas Island"},
        {'short': "CC", 'name': "Cocos (Keeling) Islands"},
        {'short': "CO", 'name': "Colombia"},
        {'short': "KM", 'name': "Comoros"},
        {'short': "CG", 'name': "Congo"},
        {'short': "CD", 'name': "Congo, the Democratic Republic of the"},
        {'short': "CK", 'name': "Cook Islands"},
        {'short': "CR", 'name': "Costa Rica"},
        {'short': "CI", 'name': "Cote d'Ivoire"},
        {'short': "HR", 'name': "Croatia (Hrvatska)"},
        {'short': "CU", 'name': "Cuba"},
        {'short': "CY", 'name': "Cyprus"},
        {'short': "CZ", 'name': "Czech Republic"},
        {'short': "DK", 'name': "Denmark"},
        {'short': "DJ", 'name': "Djibouti"},
        {'short': "DM", 'name': "Dominica"},
        {'short': "DO", 'name': "Dominican Republic"},
        {'short': "TP", 'name': "East Timor"},
        {'short': "EC", 'name': "Ecuador"},
        {'short': "EG", 'name': "Egypt"},
        {'short': "SV", 'name': "El Salvador"},
        {'short': "GQ", 'name': "Equatorial Guinea"},
        {'short': "ER", 'name': "Eritrea"},
        {'short': "EE", 'name': "Estonia"},
        {'short': "ET", 'name': "Ethiopia"},
        {'short': "FK", 'name': "Falkland Islands (Malvinas)"},
        {'short': "FO", 'name': "Faroe Islands"},
        {'short': "FJ", 'name': "Fiji"},
        {'short': "FI", 'name': "Finland"},
        {'short': "FR", 'name': "France"},
        {'short': "FX", 'name': "France, Metropolitan"},
        {'short': "GF", 'name': "French Guiana"},
        {'short': "PF", 'name': "French Polynesia"},
        {'short': "TF", 'name': "French Southern Territories"},
        {'short': "GA", 'name': "Gabon"},
        {'short': "GM", 'name': "Gambia"},
        {'short': "GE", 'name': "Georgia"},
        {'short': "DE", 'name': "Germany"},
        {'short': "GH", 'name': "Ghana"},
        {'short': "GI", 'name': "Gibraltar"},
        {'short': "GR", 'name': "Greece"},
        {'short': "GL", 'name': "Greenland"},
        {'short': "GD", 'name': "Grenada"},
        {'short': "GP", 'name': "Guadeloupe"},
        {'short': "GU", 'name': "Guam"},
        {'short': "GT", 'name': "Guatemala"},
        {'short': "GN", 'name': "Guinea"},
        {'short': "GW", 'name': "Guinea-Bissau"},
        {'short': "GY", 'name': "Guyana"},
        {'short': "HT", 'name': "Haiti"},
        {'short': "HM", 'name': "Heard and Mc Donald Islands"},
        {'short': "VA", 'name': "Holy See (Vatican City State)"},
        {'short': "HN", 'name': "Honduras"},
        {'short': "HK", 'name': "Hong Kong"},
        {'short': "HU", 'name': "Hungary"},
        {'short': "IS", 'name': "Iceland"},
        {'short': "IN", 'name': "India"},
        {'short': "ID", 'name': "Indonesia"},
        {'short': "IR", 'name': "Iran (Islamic Republic of)"},
        {'short': "IQ", 'name': "Iraq"},
        {'short': "IE", 'name': "Ireland"},
        {'short': "IL", 'name': "Israel"},
        {'short': "IT", 'name': "Italy"},
        {'short': "JM", 'name': "Jamaica"},
        {'short': "JP", 'name': "Japan"},
        {'short': "JO", 'name': "Jordan"},
        {'short': "KZ", 'name': "Kazakhstan"},
        {'short': "KE", 'name': "Kenya"},
        {'short': "KI", 'name': "Kiribati"},
        {'short': "KP", 'name': "Korea, Democratic People's Republic of"},
        {'short': "KR", 'name': "Korea, Republic of"},
        {'short': "KW", 'name': "Kuwait"},
        {'short': "KG", 'name': "Kyrgyzstan"},
        {'short': "LA", 'name': "Lao People's Democratic Republic"},
        {'short': "LV", 'name': "Latvia"},
        {'short': "LB", 'name': "Lebanon"},
        {'short': "LS", 'name': "Lesotho"},
        {'short': "LR", 'name': "Liberia"},
        {'short': "LY", 'name': "Libyan Arab Jamahiriya"},
        {'short': "LI", 'name': "Liechtenstein"},
        {'short': "LT", 'name': "Lithuania"},
        {'short': "LU", 'name': "Luxembourg"},
        {'short': "MO", 'name': "Macau"},
        {'short': "MK", 'name': "Macedonia, The Former Yugoslav Republic of"},
        {'short': "MG", 'name': "Madagascar"},
        {'short': "MW", 'name': "Malawi"},
        {'short': "MY", 'name': "Malaysia"},
        {'short': "MV", 'name': "Maldives"},
        {'short': "ML", 'name': "Mali"},
        {'short': "MT", 'name': "Malta"},
        {'short': "MH", 'name': "Marshall Islands"},
        {'short': "MQ", 'name': "Martinique"},
        {'short': "MR", 'name': "Mauritania"},
        {'short': "MU", 'name': "Mauritius"},
        {'short': "YT", 'name': "Mayotte"},
        {'short': "MX", 'name': "Mexico"},
        {'short': "FM", 'name': "Micronesia, Federated States of"},
        {'short': "MD", 'name': "Moldova, Republic of"},
        {'short': "MC", 'name': "Monaco"},
        {'short': "MN", 'name': "Mongolia"},
        {'short': "MS", 'name': "Montserrat"},
        {'short': "MA", 'name': "Morocco"},
        {'short': "MZ", 'name': "Mozambique"},
        {'short': "MM", 'name': "Myanmar"},
        {'short': "NA", 'name': "Namibia"},
        {'short': "NR", 'name': "Nauru"},
        {'short': "NP", 'name': "Nepal"},
        {'short': "NL", 'name': "Netherlands"},
        {'short': "AN", 'name': "Netherlands Antilles"},
        {'short': "NC", 'name': "New Caledonia"},
        {'short': "NZ", 'name': "New Zealand"},
        {'short': "NI", 'name': "Nicaragua"},
        {'short': "NE", 'name': "Niger"},
        {'short': "NG", 'name': "Nigeria"},
        {'short': "NU", 'name': "Niue"},
        {'short': "NF", 'name': "Norfolk Island"},
        {'short': "MP", 'name': "Northern Mariana Islands"},
        {'short': "NO", 'name': "Norway"},
        {'short': "OM", 'name': "Oman"},
        {'short': "PK", 'name': "Pakistan"},
        {'short': "PW", 'name': "Palau"},
        {'short': "PA", 'name': "Panama"},
        {'short': "PG", 'name': "Papua New Guinea"},
        {'short': "PY", 'name': "Paraguay"},
        {'short': "PE", 'name': "Peru"},
        {'short': "PH", 'name': "Philippines"},
        {'short': "PN", 'name': "Pitcairn"},
        {'short': "PL", 'name': "Poland"},
        {'short': "PT", 'name': "Portugal"},
        {'short': "PR", 'name': "Puerto Rico"},
        {'short': "QA", 'name': "Qatar"},
        {'short': "RE", 'name': "Reunion"},
        {'short': "RO", 'name': "Romania"},
        {'short': "RU", 'name': "Russian Federation"},
        {'short': "RW", 'name': "Rwanda"},
        {'short': "KN", 'name': "Saint Kitts and Nevis"},
        {'short': "LC", 'name': "Saint LUCIA"},
        {'short': "VC", 'name': "Saint Vincent and the Grenadines"},
        {'short': "WS", 'name': "Samoa"},
        {'short': "SM", 'name': "San Marino"},
        {'short': "ST", 'name': "Sao Tome and Principe"},
        {'short': "SA", 'name': "Saudi Arabia"},
        {'short': "SN", 'name': "Senegal"},
        {'short': "SC", 'name': "Seychelles"},
        {'short': "SL", 'name': "Sierra Leone"},
        {'short': "SG", 'name': "Singapore"},
        {'short': "SK", 'name': "Slovakia (Slovak Republic)"},
        {'short': "SI", 'name': "Slovenia"},
        {'short': "SB", 'name': "Solomon Islands"},
        {'short': "SO", 'name': "Somalia"},
        {'short': "ZA", 'name': "South Africa"},
        {'short': "GS", 'name': "South Georgia and the South Sandwich Islands"},
        {'short': "ES", 'name': "Spain"},
        {'short': "LK", 'name': "Sri Lanka"},
        {'short': "SH", 'name': "St. Helena"},
        {'short': "PM", 'name': "St. Pierre and Miquelon"},
        {'short': "SD", 'name': "Sudan"},
        {'short': "SR", 'name': "Suri'name'"},
        {'short': "SJ", 'name': "Svalbard and Jan Mayen Islands"},
        {'short': "SZ", 'name': "Swaziland"},
        {'short': "SE", 'name': "Sweden"},
        {'short': "CH", 'name': "Switzerland"},
        {'short': "SY", 'name': "Syrian Arab Republic"},
        {'short': "TW", 'name': "Taiwan, Province of China"},
        {'short': "TJ", 'name': "Tajikistan"},
        {'short': "TZ", 'name': "Tanzania, United Republic of"},
        {'short': "TH", 'name': "Thailand"},
        {'short': "TG", 'name': "Togo"},
        {'short': "TK", 'name': "Tokelau"},
        {'short': "TO", 'name': "Tonga"},
        {'short': "TT", 'name': "Trinidad and Tobago"},
        {'short': "TN", 'name': "Tunisia"},
        {'short': "TR", 'name': "Turkey"},
        {'short': "TM", 'name': "Turkmenistan"},
        {'short': "TC", 'name': "Turks and Caicos Islands"},
        {'short': "TV", 'name': "Tuvalu"},
        {'short': "UG", 'name': "Uganda"},
        {'short': "UA", 'name': "Ukraine"},
        {'short': "AE", 'name': "United Arab Emirates"},
        {'short': "GB", 'name': "United Kingdom"},
        {'short': "US", 'name': "United States"},
        {'short': "UM", 'name': "United States Minor Outlying Islands"},
        {'short': "UY", 'name': "Uruguay"},
        {'short': "UZ", 'name': "Uzbekistan"},
        {'short': "VU", 'name': "Vanuatu"},
        {'short': "VE", 'name': "Venezuela"},
        {'short': "VN", 'name': "Viet Nam"},
        {'short': "VG", 'name': "Virgin Islands (British)"},
        {'short': "VI", 'name': "Virgin Islands (U.S.)"},
        {'short': "WF", 'name': "Wallis and Futuna Islands"},
        {'short': "EH", 'name': "Western Sahara"},
        {'short': "YE", 'name': "Yemen"},
        {'short': "YU", 'name': "Yugoslavia"},
        {'short': "ZM", 'name': "Zambia"},
        {'short': "ZW", 'name': "Zimbabwe"}
    ]