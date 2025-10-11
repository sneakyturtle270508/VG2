# -*- coding: utf-8 -*-
# @Author: William Berge Groensberg
# @Date:   2025-10-04 21:55:53
# @Last Modified by:   William Berge Groensberg
# @Last Modified time: 2025-10-04 22:11:48
def csv_to_ics(csv_text):
    # Split lines, handle potential encoding issues
    lines = csv_text.strip().split('\n')
    headers = [h.strip() for h in lines[0].split(',')]
    
    # Map header names to column indices
    name_idx = headers.index('Name')
    start_idx = headers.index('Start Date')
    end_idx = headers.index('End Date')
    dag_idx = headers.index('Dag')
    rom_idx = headers.index('Rom')
    klasse_idx = headers.index('Klasse/Kode')
    type_idx = headers.index('Type')

    ics_lines = [
        'BEGIN:VCALENDAR',
        'VERSION:2.0',
        'PRODID:-//CSV to ICS Converter//EN'
    ]

    for line in lines[1:]:
        fields = [f.strip() for f in line.split(',')]
        summary = fields[name_idx]
        dtstart = fields[start_idx].replace('-', '').replace(':', '').replace('T', 'T')
        dtend = fields[end_idx].replace('-', '').replace(':', '').replace('T', 'T')
        description = f"{fields[type_idx]} - {fields[klasse_idx]}"
        location = fields[rom_idx]
        
        # Remove invalid characters and fix malformed datetime if needed
        if len(dtstart) != 15: continue
        if len(dtend) != 15: continue

        ics_event = [
            'BEGIN:VEVENT',
            f'SUMMARY:{summary}',
            f'DTSTART:{dtstart}',
            f'DTEND:{dtend}',
            f'DESCRIPTION:{description}',
            f'LOCATION:{location}',
            'END:VEVENT'
        ]
        ics_lines.extend(ics_event)

    ics_lines.append('END:VCALENDAR')
    return '\n'.join(ics_lines)

# Paste your CSV data into the variable below:
csv_text = """Name,Start Date,End Date,Dag,Rom,Klasse/Kode,Type
Samfunnskunnskap,2025-10-13T08:00:00,2025-10-13T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2025-10-13T08:50:00,2025-10-13T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2025-10-13T09:45:00,2025-10-13T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-10-13T10:35:00,2025-10-13T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-10-13T12:10:00,2025-10-1<3T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2025-10-13T13:00:00,2025-10-13T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2025-10-13T13:55:00,2025-10-13T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2025-10-14T08:00:00,2025-10-14T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-10-14T08:50:00,2025-10-14T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-10-14T09:45:00,2025-10-14T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-10-14T10:35:00,2025-10-14T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2025-10-14T12:10:00,2025-10-14T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-10-14T13:00:00,2025-10-14T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2025-10-14T13:55:00,2025-10-14T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2025-10-15T08:00:00,2025-10-15T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2025-10-16T08:00:00,2025-10-16T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-10-16T08:50:00,2025-10-16T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-10-16T09:45:00,2025-10-16T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-10-16T10:35:00,2025-10-16T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2025-10-16T12:10:00,2025-10-16T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2025-10-16T13:00:00,2025-10-16T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2025-10-17T08:00:00,2025-10-17T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2025-10-17T08:50:00,2025-10-17T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-10-17T09:45:00,2025-10-17T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2025-10-17T12:10:00,2025-10-17T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-10-17T13:00:00,2025-10-17T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2025-10-17T14:45:00,2025-10-17T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Name,Start Date,End Date,Dag,Rom,Klasse/Kode,Type
Samfunnskunnskap,2025-10-13T08:00:00,2025-10-13T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2025-10-13T08:50:00,2025-10-13T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2025-10-13T09:45:00,2025-10-13T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-10-13T10:35:00,2025-10-13T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-10-13T12:10:00,2025-10-1<3T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2025-10-13T13:00:00,2025-10-13T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2025-10-13T13:55:00,2025-10-13T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2025-10-14T08:00:00,2025-10-14T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-10-14T08:50:00,2025-10-14T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-10-14T09:45:00,2025-10-14T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-10-14T10:35:00,2025-10-14T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2025-10-14T12:10:00,2025-10-14T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-10-14T13:00:00,2025-10-14T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2025-10-14T13:55:00,2025-10-14T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2025-10-15T08:00:00,2025-10-15T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2025-10-16T08:00:00,2025-10-16T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-10-16T08:50:00,2025-10-16T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-10-16T09:45:00,2025-10-16T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-10-16T10:35:00,2025-10-16T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2025-10-16T12:10:00,2025-10-16T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2025-10-16T13:00:00,2025-10-16T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2025-10-17T08:00:00,2025-10-17T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2025-10-17T08:50:00,2025-10-17T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-10-17T09:45:00,2025-10-17T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2025-10-17T12:10:00,2025-10-17T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-10-17T13:00:00,2025-10-17T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2025-10-17T14:45:00,2025-10-17T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2025-10-20T08:00:00,2025-10-20T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2025-10-20T08:50:00,2025-10-20T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2025-10-20T09:45:00,2025-10-20T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-10-20T10:35:00,2025-10-20T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-10-20T12:10:00,2025-10-20T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2025-10-20T13:00:00,2025-10-20T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2025-10-20T13:55:00,2025-10-20T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2025-10-21T08:00:00,2025-10-21T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-10-21T08:50:00,2025-10-21T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-10-21T09:45:00,2025-10-21T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-10-21T10:35:00,2025-10-21T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2025-10-21T12:10:00,2025-10-21T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-10-21T13:00:00,2025-10-21T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2025-10-21T13:55:00,2025-10-21T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2025-10-22T08:00:00,2025-10-22T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2025-10-23T08:00:00,2025-10-23T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-10-23T08:50:00,2025-10-23T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-10-23T09:45:00,2025-10-23T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-10-23T10:35:00,2025-10-23T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2025-10-23T12:10:00,2025-10-23T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2025-10-23T13:00:00,2025-10-23T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2025-10-24T08:00:00,2025-10-24T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2025-10-24T08:50:00,2025-10-24T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-10-24T09:45:00,2025-10-24T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2025-10-24T12:10:00,2025-10-24T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-10-24T13:00:00,2025-10-24T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2025-10-24T14:45:00,2025-10-24T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2025-10-27T08:00:00,2025-10-27T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2025-10-27T08:50:00,2025-10-27T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2025-10-27T09:45:00,2025-10-27T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-10-27T10:35:00,2025-10-27T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-10-27T12:10:00,2025-10-27T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2025-10-27T13:00:00,2025-10-27T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2025-10-27T13:55:00,2025-10-27T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2025-10-28T08:00:00,2025-10-28T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-10-28T08:50:00,2025-10-28T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-10-28T09:45:00,2025-10-28T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-10-28T10:35:00,2025-10-28T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2025-10-28T12:10:00,2025-10-28T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-10-28T13:00:00,2025-10-28T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2025-10-28T13:55:00,2025-10-28T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2025-10-29T08:00:00,2025-10-29T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2025-10-30T08:00:00,2025-10-30T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-10-30T08:50:00,2025-10-30T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-10-30T09:45:00,2025-10-30T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-10-30T10:35:00,2025-10-30T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2025-10-30T12:10:00,2025-10-30T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2025-10-30T13:00:00,2025-10-30T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2025-10-31T08:00:00,2025-10-31T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2025-10-31T08:50:00,2025-10-31T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-10-31T09:45:00,2025-10-31T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2025-10-31T12:10:00,2025-10-31T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-10-31T13:00:00,2025-10-31T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2025-10-31T14:45:00,2025-10-31T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2025-11-03T08:00:00,2025-11-03T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2025-11-03T08:50:00,2025-11-03T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2025-11-03T09:45:00,2025-11-03T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-11-03T10:35:00,2025-11-03T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-11-03T12:10:00,2025-11-03T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2025-11-03T13:00:00,2025-11-03T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2025-11-03T13:55:00,2025-11-03T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2025-11-04T08:00:00,2025-11-04T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-11-04T08:50:00,2025-11-04T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-11-04T09:45:00,2025-11-04T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-11-04T10:35:00,2025-11-04T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2025-11-04T12:10:00,2025-11-04T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-11-04T13:00:00,2025-11-04T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2025-11-04T13:55:00,2025-11-04T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2025-11-05T08:00:00,2025-11-05T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2025-11-06T08:00:00,2025-11-06T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-11-06T08:50:00,2025-11-06T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-11-06T09:45:00,2025-11-06T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-11-06T10:35:00,2025-11-06T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2025-11-06T12:10:00,2025-11-06T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2025-11-06T13:00:00,2025-11-06T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2025-11-07T08:00:00,2025-11-07T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2025-11-07T08:50:00,2025-11-07T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-11-07T09:45:00,2025-11-07T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2025-11-07T12:10:00,2025-11-07T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-11-07T13:00:00,2025-11-07T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2025-11-07T14:45:00,2025-11-07T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2025-11-10T08:00:00,2025-11-10T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2025-11-10T08:50:00,2025-11-10T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2025-11-10T09:45:00,2025-11-10T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-11-10T10:35:00,2025-11-10T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-11-10T12:10:00,2025-11-10T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2025-11-10T13:00:00,2025-11-10T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2025-11-10T13:55:00,2025-11-10T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2025-11-11T08:00:00,2025-11-11T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-11-11T08:50:00,2025-11-11T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-11-11T09:45:00,2025-11-11T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-11-11T10:35:00,2025-11-11T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2025-11-11T12:10:00,2025-11-11T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-11-11T13:00:00,2025-11-11T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2025-11-11T13:55:00,2025-11-11T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2025-11-12T08:00:00,2025-11-12T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2025-11-13T08:00:00,2025-11-13T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-11-13T08:50:00,2025-11-13T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-11-13T09:45:00,2025-11-13T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-11-13T10:35:00,2025-11-13T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2025-11-13T12:10:00,2025-11-13T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2025-11-13T13:00:00,2025-11-13T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2025-11-14T08:00:00,2025-11-14T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2025-11-14T08:50:00,2025-11-14T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-11-14T09:45:00,2025-11-14T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2025-11-14T12:10:00,2025-11-14T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-11-14T13:00:00,2025-11-14T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2025-11-14T14:45:00,2025-11-14T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2025-11-17T08:00:00,2025-11-17T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2025-11-17T08:50:00,2025-11-17T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2025-11-17T09:45:00,2025-11-17T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-11-17T10:35:00,2025-11-17T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-11-17T12:10:00,2025-11-17T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2025-11-17T13:00:00,2025-11-17T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2025-11-17T13:55:00,2025-11-17T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2025-11-18T08:00:00,2025-11-18T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-11-18T08:50:00,2025-11-18T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-11-18T09:45:00,2025-11-18T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-11-18T10:35:00,2025-11-18T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2025-11-18T12:10:00,2025-11-18T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-11-18T13:00:00,2025-11-18T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2025-11-18T13:55:00,2025-11-18T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2025-11-19T08:00:00,2025-11-19T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2025-11-20T08:00:00,2025-11-20T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-11-20T08:50:00,2025-11-20T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-11-20T09:45:00,2025-11-20T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-11-20T10:35:00,2025-11-20T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2025-11-20T12:10:00,2025-11-20T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2025-11-20T13:00:00,2025-11-20T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2025-11-21T08:00:00,2025-11-21T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2025-11-21T08:50:00,2025-11-21T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-11-21T09:45:00,2025-11-21T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2025-11-21T12:10:00,2025-11-21T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-11-21T13:00:00,2025-11-21T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2025-11-21T14:45:00,2025-11-21T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2025-11-24T08:00:00,2025-11-24T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2025-11-24T08:50:00,2025-11-24T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2025-11-24T09:45:00,2025-11-24T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-11-24T10:35:00,2025-11-24T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-11-24T12:10:00,2025-11-24T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2025-11-24T13:00:00,2025-11-24T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2025-11-24T13:55:00,2025-11-24T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2025-11-25T08:00:00,2025-11-25T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-11-25T08:50:00,2025-11-25T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-11-25T09:45:00,2025-11-25T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-11-25T10:35:00,2025-11-25T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2025-11-25T12:10:00,2025-11-25T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-11-25T13:00:00,2025-11-25T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2025-11-25T13:55:00,2025-11-25T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2025-11-26T08:00:00,2025-11-26T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2025-11-27T08:00:00,2025-11-27T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-11-27T08:50:00,2025-11-27T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-11-27T09:45:00,2025-11-27T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-11-27T10:35:00,2025-11-27T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2025-11-27T12:10:00,2025-11-27T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2025-11-27T13:00:00,2025-11-27T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2025-11-28T08:00:00,2025-11-28T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2025-11-28T08:50:00,2025-11-28T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-11-28T09:45:00,2025-11-28T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2025-11-28T12:10:00,2025-11-28T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-11-28T13:00:00,2025-11-28T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2025-11-28T14:45:00,2025-11-28T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2025-12-01T08:00:00,2025-12-01T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2025-12-01T08:50:00,2025-12-01T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2025-12-01T09:45:00,2025-12-01T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-12-01T10:35:00,2025-12-01T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-12-01T12:10:00,2025-12-01T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2025-12-01T13:00:00,2025-12-01T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2025-12-01T13:55:00,2025-12-01T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2025-12-02T08:00:00,2025-12-02T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-12-02T08:50:00,2025-12-02T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-12-02T09:45:00,2025-12-02T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-12-02T10:35:00,2025-12-02T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2025-12-02T12:10:00,2025-12-02T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-12-02T13:00:00,2025-12-02T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2025-12-02T13:55:00,2025-12-02T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2025-12-03T08:00:00,2025-12-03T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2025-12-04T08:00:00,2025-12-04T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-12-04T08:50:00,2025-12-04T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-12-04T09:45:00,2025-12-04T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-12-04T10:35:00,2025-12-04T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2025-12-04T12:10:00,2025-12-04T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2025-12-04T13:00:00,2025-12-04T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2025-12-05T08:00:00,2025-12-05T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2025-12-05T08:50:00,2025-12-05T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-12-05T09:45:00,2025-12-05T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2025-12-05T12:10:00,2025-12-05T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-12-05T13:00:00,2025-12-05T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2025-12-05T14:45:00,2025-12-05T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2025-12-08T08:00:00,2025-12-08T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2025-12-08T08:50:00,2025-12-08T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2025-12-08T09:45:00,2025-12-08T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-12-08T10:35:00,2025-12-08T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-12-08T12:10:00,2025-12-08T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2025-12-08T13:00:00,2025-12-08T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2025-12-08T13:55:00,2025-12-08T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2025-12-09T08:00:00,2025-12-09T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-12-09T08:50:00,2025-12-09T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-12-09T09:45:00,2025-12-09T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-12-09T10:35:00,2025-12-09T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2025-12-09T12:10:00,2025-12-09T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-12-09T13:00:00,2025-12-09T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2025-12-09T13:55:00,2025-12-09T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2025-12-10T08:00:00,2025-12-10T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2025-12-11T08:00:00,2025-12-11T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-12-11T08:50:00,2025-12-11T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-12-11T09:45:00,2025-12-11T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-12-11T10:35:00,2025-12-11T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2025-12-11T12:10:00,2025-12-11T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2025-12-11T13:00:00,2025-12-11T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2025-12-12T08:00:00,2025-12-12T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2025-12-12T08:50:00,2025-12-12T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-12-12T09:45:00,2025-12-12T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2025-12-12T12:10:00,2025-12-12T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-12-12T13:00:00,2025-12-12T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2025-12-12T14:45:00,2025-12-12T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2025-12-15T08:00:00,2025-12-15T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2025-12-15T08:50:00,2025-12-15T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2025-12-15T09:45:00,2025-12-15T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-12-15T10:35:00,2025-12-15T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-12-15T12:10:00,2025-12-15T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2025-12-15T13:00:00,2025-12-15T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2025-12-15T13:55:00,2025-12-15T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2025-12-16T08:00:00,2025-12-16T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-12-16T08:50:00,2025-12-16T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-12-16T09:45:00,2025-12-16T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-12-16T10:35:00,2025-12-16T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2025-12-16T12:10:00,2025-12-16T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-12-16T13:00:00,2025-12-16T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2025-12-16T13:55:00,2025-12-16T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2025-12-17T08:00:00,2025-12-17T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2025-12-18T08:00:00,2025-12-18T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-12-18T08:50:00,2025-12-18T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-12-18T09:45:00,2025-12-18T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-12-18T10:35:00,2025-12-18T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2025-12-18T12:10:00,2025-12-18T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2025-12-18T13:00:00,2025-12-18T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2025-12-19T08:00:00,2025-12-19T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2025-12-19T08:50:00,2025-12-19T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-12-19T09:45:00,2025-12-19T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2025-12-19T12:10:00,2025-12-19T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-12-19T13:00:00,2025-12-19T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2025-12-19T14:45:00,2025-12-19T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2025-12-22T08:00:00,2025-12-22T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2025-12-22T08:50:00,2025-12-22T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2025-12-22T09:45:00,2025-12-22T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-12-22T10:35:00,2025-12-22T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-12-22T12:10:00,2025-12-22T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2025-12-22T13:00:00,2025-12-22T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2025-12-22T13:55:00,2025-12-22T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2025-12-23T08:00:00,2025-12-23T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-12-23T08:50:00,2025-12-23T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-12-23T09:45:00,2025-12-23T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-12-23T10:35:00,2025-12-23T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2025-12-23T12:10:00,2025-12-23T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-12-23T13:00:00,2025-12-23T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2025-12-23T13:55:00,2025-12-23T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2025-12-24T08:00:00,2025-12-24T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2025-12-25T08:00:00,2025-12-25T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-12-25T08:50:00,2025-12-25T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-12-25T09:45:00,2025-12-25T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-12-25T10:35:00,2025-12-25T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2025-12-25T12:10:00,2025-12-25T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2025-12-25T13:00:00,2025-12-25T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2025-12-26T08:00:00,2025-12-26T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2025-12-26T08:50:00,2025-12-26T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-12-26T09:45:00,2025-12-26T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2025-12-26T12:10:00,2025-12-26T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-12-26T13:00:00,2025-12-26T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2025-12-26T14:45:00,2025-12-26T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2025-12-29T08:00:00,2025-12-29T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2025-12-29T08:50:00,2025-12-29T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2025-12-29T09:45:00,2025-12-29T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-12-29T10:35:00,2025-12-29T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2025-12-29T12:10:00,2025-12-29T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2025-12-29T13:00:00,2025-12-29T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2025-12-29T13:55:00,2025-12-29T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2025-12-30T08:00:00,2025-12-30T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-12-30T08:50:00,2025-12-30T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-12-30T09:45:00,2025-12-30T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2025-12-30T10:35:00,2025-12-30T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2025-12-30T12:10:00,2025-12-30T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2025-12-30T13:00:00,2025-12-30T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2025-12-30T13:55:00,2025-12-30T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2025-12-31T08:00:00,2025-12-31T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2026-01-01T08:00:00,2026-01-01T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-01-01T08:50:00,2026-01-01T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-01-01T09:45:00,2026-01-01T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-01-01T10:35:00,2026-01-01T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2026-01-01T12:10:00,2026-01-01T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2026-01-01T13:00:00,2026-01-01T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2026-01-02T08:00:00,2026-01-02T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-01-02T08:50:00,2026-01-02T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-01-02T09:45:00,2026-01-02T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2026-01-02T12:10:00,2026-01-02T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-01-02T13:00:00,2026-01-02T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2026-01-02T14:45:00,2026-01-02T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2026-01-05T08:00:00,2026-01-05T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2026-01-05T08:50:00,2026-01-05T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-01-05T09:45:00,2026-01-05T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-01-05T10:35:00,2026-01-05T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-01-05T12:10:00,2026-01-05T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2026-01-05T13:00:00,2026-01-05T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2026-01-05T13:55:00,2026-01-05T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2026-01-06T08:00:00,2026-01-06T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-01-06T08:50:00,2026-01-06T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-01-06T09:45:00,2026-01-06T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-01-06T10:35:00,2026-01-06T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2026-01-06T12:10:00,2026-01-06T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-01-06T13:00:00,2026-01-06T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2026-01-06T13:55:00,2026-01-06T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2026-01-07T08:00:00,2026-01-07T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2026-01-08T08:00:00,2026-01-08T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-01-08T08:50:00,2026-01-08T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-01-08T09:45:00,2026-01-08T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-01-08T10:35:00,2026-01-08T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2026-01-08T12:10:00,2026-01-08T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2026-01-08T13:00:00,2026-01-08T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2026-01-09T08:00:00,2026-01-09T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-01-09T08:50:00,2026-01-09T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-01-09T09:45:00,2026-01-09T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2026-01-09T12:10:00,2026-01-09T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-01-09T13:00:00,2026-01-09T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2026-01-09T14:45:00,2026-01-09T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2026-01-12T08:00:00,2026-01-12T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2026-01-12T08:50:00,2026-01-12T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-01-12T09:45:00,2026-01-12T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-01-12T10:35:00,2026-01-12T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-01-12T12:10:00,2026-01-12T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2026-01-12T13:00:00,2026-01-12T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2026-01-12T13:55:00,2026-01-12T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2026-01-13T08:00:00,2026-01-13T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-01-13T08:50:00,2026-01-13T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-01-13T09:45:00,2026-01-13T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-01-13T10:35:00,2026-01-13T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2026-01-13T12:10:00,2026-01-13T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-01-13T13:00:00,2026-01-13T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2026-01-13T13:55:00,2026-01-13T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2026-01-14T08:00:00,2026-01-14T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2026-01-15T08:00:00,2026-01-15T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-01-15T08:50:00,2026-01-15T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-01-15T09:45:00,2026-01-15T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-01-15T10:35:00,2026-01-15T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2026-01-15T12:10:00,2026-01-15T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2026-01-15T13:00:00,2026-01-15T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2026-01-16T08:00:00,2026-01-16T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-01-16T08:50:00,2026-01-16T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-01-16T09:45:00,2026-01-16T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2026-01-16T12:10:00,2026-01-16T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-01-16T13:00:00,2026-01-16T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2026-01-16T14:45:00,2026-01-16T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2026-01-19T08:00:00,2026-01-19T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2026-01-19T08:50:00,2026-01-19T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-01-19T09:45:00,2026-01-19T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-01-19T10:35:00,2026-01-19T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-01-19T12:10:00,2026-01-19T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2026-01-19T13:00:00,2026-01-19T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2026-01-19T13:55:00,2026-01-19T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2026-01-20T08:00:00,2026-01-20T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-01-20T08:50:00,2026-01-20T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-01-20T09:45:00,2026-01-20T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-01-20T10:35:00,2026-01-20T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2026-01-20T12:10:00,2026-01-20T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-01-20T13:00:00,2026-01-20T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2026-01-20T13:55:00,2026-01-20T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2026-01-21T08:00:00,2026-01-21T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2026-01-22T08:00:00,2026-01-22T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-01-22T08:50:00,2026-01-22T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-01-22T09:45:00,2026-01-22T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-01-22T10:35:00,2026-01-22T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2026-01-22T12:10:00,2026-01-22T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2026-01-22T13:00:00,2026-01-22T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2026-01-23T08:00:00,2026-01-23T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-01-23T08:50:00,2026-01-23T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-01-23T09:45:00,2026-01-23T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2026-01-23T12:10:00,2026-01-23T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-01-23T13:00:00,2026-01-23T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2026-01-23T14:45:00,2026-01-23T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2026-01-26T08:00:00,2026-01-26T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2026-01-26T08:50:00,2026-01-26T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-01-26T09:45:00,2026-01-26T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-01-26T10:35:00,2026-01-26T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-01-26T12:10:00,2026-01-26T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2026-01-26T13:00:00,2026-01-26T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2026-01-26T13:55:00,2026-01-26T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2026-01-27T08:00:00,2026-01-27T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-01-27T08:50:00,2026-01-27T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-01-27T09:45:00,2026-01-27T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-01-27T10:35:00,2026-01-27T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2026-01-27T12:10:00,2026-01-27T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-01-27T13:00:00,2026-01-27T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2026-01-27T13:55:00,2026-01-27T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2026-01-28T08:00:00,2026-01-28T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2026-01-29T08:00:00,2026-01-29T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-01-29T08:50:00,2026-01-29T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-01-29T09:45:00,2026-01-29T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-01-29T10:35:00,2026-01-29T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2026-01-29T12:10:00,2026-01-29T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2026-01-29T13:00:00,2026-01-29T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2026-01-30T08:00:00,2026-01-30T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-01-30T08:50:00,2026-01-30T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-01-30T09:45:00,2026-01-30T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2026-01-30T12:10:00,2026-01-30T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-01-30T13:00:00,2026-01-30T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2026-01-30T14:45:00,2026-01-30T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2026-02-02T08:00:00,2026-02-02T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2026-02-02T08:50:00,2026-02-02T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-02-02T09:45:00,2026-02-02T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-02-02T10:35:00,2026-02-02T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-02-02T12:10:00,2026-02-02T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2026-02-02T13:00:00,2026-02-02T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2026-02-02T13:55:00,2026-02-02T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2026-02-03T08:00:00,2026-02-03T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-02-03T08:50:00,2026-02-03T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-02-03T09:45:00,2026-02-03T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-02-03T10:35:00,2026-02-03T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2026-02-03T12:10:00,2026-02-03T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-02-03T13:00:00,2026-02-03T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2026-02-03T13:55:00,2026-02-03T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2026-02-04T08:00:00,2026-02-04T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2026-02-05T08:00:00,2026-02-05T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-02-05T08:50:00,2026-02-05T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-02-05T09:45:00,2026-02-05T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-02-05T10:35:00,2026-02-05T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2026-02-05T12:10:00,2026-02-05T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2026-02-05T13:00:00,2026-02-05T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2026-02-06T08:00:00,2026-02-06T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-02-06T08:50:00,2026-02-06T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-02-06T09:45:00,2026-02-06T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2026-02-06T12:10:00,2026-02-06T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-02-06T13:00:00,2026-02-06T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2026-02-06T14:45:00,2026-02-06T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2026-02-09T08:00:00,2026-02-09T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2026-02-09T08:50:00,2026-02-09T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-02-09T09:45:00,2026-02-09T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-02-09T10:35:00,2026-02-09T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-02-09T12:10:00,2026-02-09T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2026-02-09T13:00:00,2026-02-09T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2026-02-09T13:55:00,2026-02-09T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2026-02-10T08:00:00,2026-02-10T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-02-10T08:50:00,2026-02-10T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-02-10T09:45:00,2026-02-10T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-02-10T10:35:00,2026-02-10T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2026-02-10T12:10:00,2026-02-10T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-02-10T13:00:00,2026-02-10T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2026-02-10T13:55:00,2026-02-10T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2026-02-11T08:00:00,2026-02-11T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2026-02-12T08:00:00,2026-02-12T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-02-12T08:50:00,2026-02-12T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-02-12T09:45:00,2026-02-12T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-02-12T10:35:00,2026-02-12T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2026-02-12T12:10:00,2026-02-12T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2026-02-12T13:00:00,2026-02-12T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2026-02-13T08:00:00,2026-02-13T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-02-13T08:50:00,2026-02-13T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-02-13T09:45:00,2026-02-13T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2026-02-13T12:10:00,2026-02-13T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-02-13T13:00:00,2026-02-13T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2026-02-13T14:45:00,2026-02-13T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2026-02-16T08:00:00,2026-02-16T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2026-02-16T08:50:00,2026-02-16T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-02-16T09:45:00,2026-02-16T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-02-16T10:35:00,2026-02-16T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-02-16T12:10:00,2026-02-16T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2026-02-16T13:00:00,2026-02-16T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2026-02-16T13:55:00,2026-02-16T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2026-02-17T08:00:00,2026-02-17T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-02-17T08:50:00,2026-02-17T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-02-17T09:45:00,2026-02-17T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-02-17T10:35:00,2026-02-17T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2026-02-17T12:10:00,2026-02-17T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-02-17T13:00:00,2026-02-17T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2026-02-17T13:55:00,2026-02-17T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2026-02-18T08:00:00,2026-02-18T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2026-02-19T08:00:00,2026-02-19T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-02-19T08:50:00,2026-02-19T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-02-19T09:45:00,2026-02-19T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-02-19T10:35:00,2026-02-19T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2026-02-19T12:10:00,2026-02-19T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2026-02-19T13:00:00,2026-02-19T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2026-02-20T08:00:00,2026-02-20T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-02-20T08:50:00,2026-02-20T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-02-20T09:45:00,2026-02-20T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2026-02-20T12:10:00,2026-02-20T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-02-20T13:00:00,2026-02-20T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2026-02-20T14:45:00,2026-02-20T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2026-02-23T08:00:00,2026-02-23T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2026-02-23T08:50:00,2026-02-23T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-02-23T09:45:00,2026-02-23T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-02-23T10:35:00,2026-02-23T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-02-23T12:10:00,2026-02-23T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2026-02-23T13:00:00,2026-02-23T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2026-02-23T13:55:00,2026-02-23T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2026-02-24T08:00:00,2026-02-24T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-02-24T08:50:00,2026-02-24T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-02-24T09:45:00,2026-02-24T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-02-24T10:35:00,2026-02-24T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2026-02-24T12:10:00,2026-02-24T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-02-24T13:00:00,2026-02-24T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2026-02-24T13:55:00,2026-02-24T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2026-02-25T08:00:00,2026-02-25T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2026-02-26T08:00:00,2026-02-26T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-02-26T08:50:00,2026-02-26T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-02-26T09:45:00,2026-02-26T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-02-26T10:35:00,2026-02-26T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2026-02-26T12:10:00,2026-02-26T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2026-02-26T13:00:00,2026-02-26T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2026-02-27T08:00:00,2026-02-27T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-02-27T08:50:00,2026-02-27T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-02-27T09:45:00,2026-02-27T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2026-02-27T12:10:00,2026-02-27T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-02-27T13:00:00,2026-02-27T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2026-02-27T14:45:00,2026-02-27T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2026-03-02T08:00:00,2026-03-02T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2026-03-02T08:50:00,2026-03-02T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-03-02T09:45:00,2026-03-02T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-03-02T10:35:00,2026-03-02T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-03-02T12:10:00,2026-03-02T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2026-03-02T13:00:00,2026-03-02T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2026-03-02T13:55:00,2026-03-02T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2026-03-03T08:00:00,2026-03-03T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-03-03T08:50:00,2026-03-03T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-03-03T09:45:00,2026-03-03T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-03-03T10:35:00,2026-03-03T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2026-03-03T12:10:00,2026-03-03T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-03-03T13:00:00,2026-03-03T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2026-03-03T13:55:00,2026-03-03T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2026-03-04T08:00:00,2026-03-04T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2026-03-05T08:00:00,2026-03-05T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-03-05T08:50:00,2026-03-05T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-03-05T09:45:00,2026-03-05T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-03-05T10:35:00,2026-03-05T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2026-03-05T12:10:00,2026-03-05T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2026-03-05T13:00:00,2026-03-05T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2026-03-06T08:00:00,2026-03-06T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-03-06T08:50:00,2026-03-06T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-03-06T09:45:00,2026-03-06T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2026-03-06T12:10:00,2026-03-06T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-03-06T13:00:00,2026-03-06T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2026-03-06T14:45:00,2026-03-06T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2026-03-09T08:00:00,2026-03-09T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2026-03-09T08:50:00,2026-03-09T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-03-09T09:45:00,2026-03-09T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-03-09T10:35:00,2026-03-09T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-03-09T12:10:00,2026-03-09T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2026-03-09T13:00:00,2026-03-09T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2026-03-09T13:55:00,2026-03-09T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2026-03-10T08:00:00,2026-03-10T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-03-10T08:50:00,2026-03-10T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-03-10T09:45:00,2026-03-10T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-03-10T10:35:00,2026-03-10T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2026-03-10T12:10:00,2026-03-10T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-03-10T13:00:00,2026-03-10T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2026-03-10T13:55:00,2026-03-10T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2026-03-11T08:00:00,2026-03-11T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2026-03-12T08:00:00,2026-03-12T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-03-12T08:50:00,2026-03-12T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-03-12T09:45:00,2026-03-12T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-03-12T10:35:00,2026-03-12T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2026-03-12T12:10:00,2026-03-12T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2026-03-12T13:00:00,2026-03-12T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2026-03-13T08:00:00,2026-03-13T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-03-13T08:50:00,2026-03-13T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-03-13T09:45:00,2026-03-13T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2026-03-13T12:10:00,2026-03-13T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-03-13T13:00:00,2026-03-13T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2026-03-13T14:45:00,2026-03-13T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2026-03-16T08:00:00,2026-03-16T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2026-03-16T08:50:00,2026-03-16T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-03-16T09:45:00,2026-03-16T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-03-16T10:35:00,2026-03-16T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-03-16T12:10:00,2026-03-16T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2026-03-16T13:00:00,2026-03-16T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2026-03-16T13:55:00,2026-03-16T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2026-03-17T08:00:00,2026-03-17T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-03-17T08:50:00,2026-03-17T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-03-17T09:45:00,2026-03-17T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-03-17T10:35:00,2026-03-17T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2026-03-17T12:10:00,2026-03-17T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-03-17T13:00:00,2026-03-17T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2026-03-17T13:55:00,2026-03-17T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2026-03-18T08:00:00,2026-03-18T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2026-03-19T08:00:00,2026-03-19T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-03-19T08:50:00,2026-03-19T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-03-19T09:45:00,2026-03-19T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-03-19T10:35:00,2026-03-19T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2026-03-19T12:10:00,2026-03-19T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2026-03-19T13:00:00,2026-03-19T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2026-03-20T08:00:00,2026-03-20T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-03-20T08:50:00,2026-03-20T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-03-20T09:45:00,2026-03-20T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2026-03-20T12:10:00,2026-03-20T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-03-20T13:00:00,2026-03-20T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2026-03-20T14:45:00,2026-03-20T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2026-03-23T08:00:00,2026-03-23T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2026-03-23T08:50:00,2026-03-23T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-03-23T09:45:00,2026-03-23T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-03-23T10:35:00,2026-03-23T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-03-23T12:10:00,2026-03-23T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2026-03-23T13:00:00,2026-03-23T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2026-03-23T13:55:00,2026-03-23T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2026-03-24T08:00:00,2026-03-24T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-03-24T08:50:00,2026-03-24T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-03-24T09:45:00,2026-03-24T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-03-24T10:35:00,2026-03-24T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2026-03-24T12:10:00,2026-03-24T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-03-24T13:00:00,2026-03-24T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2026-03-24T13:55:00,2026-03-24T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2026-03-25T08:00:00,2026-03-25T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2026-03-26T08:00:00,2026-03-26T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-03-26T08:50:00,2026-03-26T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-03-26T09:45:00,2026-03-26T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-03-26T10:35:00,2026-03-26T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2026-03-26T12:10:00,2026-03-26T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2026-03-26T13:00:00,2026-03-26T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2026-03-27T08:00:00,2026-03-27T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-03-27T08:50:00,2026-03-27T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-03-27T09:45:00,2026-03-27T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2026-03-27T12:10:00,2026-03-27T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-03-27T13:00:00,2026-03-27T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2026-03-27T14:45:00,2026-03-27T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2026-03-30T08:00:00,2026-03-30T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2026-03-30T08:50:00,2026-03-30T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-03-30T09:45:00,2026-03-30T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-03-30T10:35:00,2026-03-30T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-03-30T12:10:00,2026-03-30T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2026-03-30T13:00:00,2026-03-30T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2026-03-30T13:55:00,2026-03-30T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2026-03-31T08:00:00,2026-03-31T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-03-31T08:50:00,2026-03-31T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-03-31T09:45:00,2026-03-31T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-03-31T10:35:00,2026-03-31T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2026-03-31T12:10:00,2026-03-31T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-03-31T13:00:00,2026-03-31T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2026-03-31T13:55:00,2026-03-31T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2026-04-01T08:00:00,2026-04-01T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2026-04-02T08:00:00,2026-04-02T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-04-02T08:50:00,2026-04-02T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-04-02T09:45:00,2026-04-02T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-04-02T10:35:00,2026-04-02T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2026-04-02T12:10:00,2026-04-02T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2026-04-02T13:00:00,2026-04-02T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2026-04-03T08:00:00,2026-04-03T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-04-03T08:50:00,2026-04-03T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-04-03T09:45:00,2026-04-03T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2026-04-03T12:10:00,2026-04-03T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-04-03T13:00:00,2026-04-03T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2026-04-03T14:45:00,2026-04-03T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2026-04-06T08:00:00,2026-04-06T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2026-04-06T08:50:00,2026-04-06T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-04-06T09:45:00,2026-04-06T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-04-06T10:35:00,2026-04-06T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-04-06T12:10:00,2026-04-06T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2026-04-06T13:00:00,2026-04-06T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2026-04-06T13:55:00,2026-04-06T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2026-04-07T08:00:00,2026-04-07T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-04-07T08:50:00,2026-04-07T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-04-07T09:45:00,2026-04-07T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-04-07T10:35:00,2026-04-07T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2026-04-07T12:10:00,2026-04-07T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-04-07T13:00:00,2026-04-07T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2026-04-07T13:55:00,2026-04-07T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2026-04-08T08:00:00,2026-04-08T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2026-04-09T08:00:00,2026-04-09T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-04-09T08:50:00,2026-04-09T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-04-09T09:45:00,2026-04-09T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-04-09T10:35:00,2026-04-09T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2026-04-09T12:10:00,2026-04-09T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2026-04-09T13:00:00,2026-04-09T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2026-04-10T08:00:00,2026-04-10T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-04-10T08:50:00,2026-04-10T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-04-10T09:45:00,2026-04-10T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2026-04-10T12:10:00,2026-04-10T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-04-10T13:00:00,2026-04-10T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2026-04-10T14:45:00,2026-04-10T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2026-04-13T08:00:00,2026-04-13T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2026-04-13T08:50:00,2026-04-13T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-04-13T09:45:00,2026-04-13T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-04-13T10:35:00,2026-04-13T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-04-13T12:10:00,2026-04-13T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2026-04-13T13:00:00,2026-04-13T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2026-04-13T13:55:00,2026-04-13T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2026-04-14T08:00:00,2026-04-14T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-04-14T08:50:00,2026-04-14T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-04-14T09:45:00,2026-04-14T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-04-14T10:35:00,2026-04-14T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2026-04-14T12:10:00,2026-04-14T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-04-14T13:00:00,2026-04-14T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2026-04-14T13:55:00,2026-04-14T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2026-04-15T08:00:00,2026-04-15T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2026-04-16T08:00:00,2026-04-16T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-04-16T08:50:00,2026-04-16T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-04-16T09:45:00,2026-04-16T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-04-16T10:35:00,2026-04-16T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2026-04-16T12:10:00,2026-04-16T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2026-04-16T13:00:00,2026-04-16T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2026-04-17T08:00:00,2026-04-17T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-04-17T08:50:00,2026-04-17T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-04-17T09:45:00,2026-04-17T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2026-04-17T12:10:00,2026-04-17T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-04-17T13:00:00,2026-04-17T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2026-04-17T14:45:00,2026-04-17T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2026-04-20T08:00:00,2026-04-20T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2026-04-20T08:50:00,2026-04-20T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-04-20T09:45:00,2026-04-20T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-04-20T10:35:00,2026-04-20T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-04-20T12:10:00,2026-04-20T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2026-04-20T13:00:00,2026-04-20T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2026-04-20T13:55:00,2026-04-20T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2026-04-21T08:00:00,2026-04-21T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-04-21T08:50:00,2026-04-21T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-04-21T09:45:00,2026-04-21T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-04-21T10:35:00,2026-04-21T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2026-04-21T12:10:00,2026-04-21T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-04-21T13:00:00,2026-04-21T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2026-04-21T13:55:00,2026-04-21T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2026-04-22T08:00:00,2026-04-22T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2026-04-23T08:00:00,2026-04-23T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-04-23T08:50:00,2026-04-23T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-04-23T09:45:00,2026-04-23T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-04-23T10:35:00,2026-04-23T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2026-04-23T12:10:00,2026-04-23T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2026-04-23T13:00:00,2026-04-23T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2026-04-24T08:00:00,2026-04-24T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-04-24T08:50:00,2026-04-24T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-04-24T09:45:00,2026-04-24T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2026-04-24T12:10:00,2026-04-24T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-04-24T13:00:00,2026-04-24T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2026-04-24T14:45:00,2026-04-24T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2026-04-27T08:00:00,2026-04-27T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2026-04-27T08:50:00,2026-04-27T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-04-27T09:45:00,2026-04-27T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-04-27T10:35:00,2026-04-27T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-04-27T12:10:00,2026-04-27T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2026-04-27T13:00:00,2026-04-27T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2026-04-27T13:55:00,2026-04-27T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2026-04-28T08:00:00,2026-04-28T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-04-28T08:50:00,2026-04-28T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-04-28T09:45:00,2026-04-28T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-04-28T10:35:00,2026-04-28T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2026-04-28T12:10:00,2026-04-28T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-04-28T13:00:00,2026-04-28T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2026-04-28T13:55:00,2026-04-28T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2026-04-29T08:00:00,2026-04-29T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2026-04-30T08:00:00,2026-04-30T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-04-30T08:50:00,2026-04-30T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-04-30T09:45:00,2026-04-30T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-04-30T10:35:00,2026-04-30T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2026-04-30T12:10:00,2026-04-30T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2026-04-30T13:00:00,2026-04-30T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2026-05-01T08:00:00,2026-05-01T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-05-01T08:50:00,2026-05-01T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-05-01T09:45:00,2026-05-01T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2026-05-01T12:10:00,2026-05-01T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-05-01T13:00:00,2026-05-01T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2026-05-01T14:45:00,2026-05-01T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2026-05-04T08:00:00,2026-05-04T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2026-05-04T08:50:00,2026-05-04T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-05-04T09:45:00,2026-05-04T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-05-04T10:35:00,2026-05-04T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-05-04T12:10:00,2026-05-04T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2026-05-04T13:00:00,2026-05-04T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2026-05-04T13:55:00,2026-05-04T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2026-05-05T08:00:00,2026-05-05T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-05-05T08:50:00,2026-05-05T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-05-05T09:45:00,2026-05-05T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-05-05T10:35:00,2026-05-05T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2026-05-05T12:10:00,2026-05-05T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-05-05T13:00:00,2026-05-05T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2026-05-05T13:55:00,2026-05-05T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2026-05-06T08:00:00,2026-05-06T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2026-05-07T08:00:00,2026-05-07T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-05-07T08:50:00,2026-05-07T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-05-07T09:45:00,2026-05-07T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-05-07T10:35:00,2026-05-07T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2026-05-07T12:10:00,2026-05-07T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2026-05-07T13:00:00,2026-05-07T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2026-05-08T08:00:00,2026-05-08T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-05-08T08:50:00,2026-05-08T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-05-08T09:45:00,2026-05-08T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2026-05-08T12:10:00,2026-05-08T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-05-08T13:00:00,2026-05-08T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2026-05-08T14:45:00,2026-05-08T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2026-05-11T08:00:00,2026-05-11T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2026-05-11T08:50:00,2026-05-11T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-05-11T09:45:00,2026-05-11T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-05-11T10:35:00,2026-05-11T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-05-11T12:10:00,2026-05-11T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2026-05-11T13:00:00,2026-05-11T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2026-05-11T13:55:00,2026-05-11T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2026-05-12T08:00:00,2026-05-12T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-05-12T08:50:00,2026-05-12T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-05-12T09:45:00,2026-05-12T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-05-12T10:35:00,2026-05-12T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2026-05-12T12:10:00,2026-05-12T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-05-12T13:00:00,2026-05-12T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2026-05-12T13:55:00,2026-05-12T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2026-05-13T08:00:00,2026-05-13T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2026-05-14T08:00:00,2026-05-14T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-05-14T08:50:00,2026-05-14T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-05-14T09:45:00,2026-05-14T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-05-14T10:35:00,2026-05-14T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2026-05-14T12:10:00,2026-05-14T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2026-05-14T13:00:00,2026-05-14T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2026-05-15T08:00:00,2026-05-15T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-05-15T08:50:00,2026-05-15T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-05-15T09:45:00,2026-05-15T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2026-05-15T12:10:00,2026-05-15T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-05-15T13:00:00,2026-05-15T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2026-05-15T14:45:00,2026-05-15T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2026-05-18T08:00:00,2026-05-18T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2026-05-18T08:50:00,2026-05-18T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-05-18T09:45:00,2026-05-18T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-05-18T10:35:00,2026-05-18T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-05-18T12:10:00,2026-05-18T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2026-05-18T13:00:00,2026-05-18T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2026-05-18T13:55:00,2026-05-18T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2026-05-19T08:00:00,2026-05-19T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-05-19T08:50:00,2026-05-19T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-05-19T09:45:00,2026-05-19T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-05-19T10:35:00,2026-05-19T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2026-05-19T12:10:00,2026-05-19T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-05-19T13:00:00,2026-05-19T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2026-05-19T13:55:00,2026-05-19T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2026-05-20T08:00:00,2026-05-20T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2026-05-21T08:00:00,2026-05-21T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-05-21T08:50:00,2026-05-21T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-05-21T09:45:00,2026-05-21T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-05-21T10:35:00,2026-05-21T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2026-05-21T12:10:00,2026-05-21T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2026-05-21T13:00:00,2026-05-21T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2026-05-22T08:00:00,2026-05-22T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-05-22T08:50:00,2026-05-22T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-05-22T09:45:00,2026-05-22T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2026-05-22T12:10:00,2026-05-22T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-05-22T13:00:00,2026-05-22T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2026-05-22T14:45:00,2026-05-22T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2026-05-25T08:00:00,2026-05-25T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2026-05-25T08:50:00,2026-05-25T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-05-25T09:45:00,2026-05-25T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-05-25T10:35:00,2026-05-25T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-05-25T12:10:00,2026-05-25T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2026-05-25T13:00:00,2026-05-25T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2026-05-25T13:55:00,2026-05-25T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2026-05-26T08:00:00,2026-05-26T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-05-26T08:50:00,2026-05-26T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-05-26T09:45:00,2026-05-26T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-05-26T10:35:00,2026-05-26T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2026-05-26T12:10:00,2026-05-26T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-05-26T13:00:00,2026-05-26T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2026-05-26T13:55:00,2026-05-26T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2026-05-27T08:00:00,2026-05-27T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2026-05-28T08:00:00,2026-05-28T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-05-28T08:50:00,2026-05-28T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-05-28T09:45:00,2026-05-28T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-05-28T10:35:00,2026-05-28T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2026-05-28T12:10:00,2026-05-28T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2026-05-28T13:00:00,2026-05-28T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2026-05-29T08:00:00,2026-05-29T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-05-29T08:50:00,2026-05-29T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-05-29T09:45:00,2026-05-29T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2026-05-29T12:10:00,2026-05-29T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-05-29T13:00:00,2026-05-29T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2026-05-29T14:45:00,2026-05-29T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2026-06-01T08:00:00,2026-06-01T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2026-06-01T08:50:00,2026-06-01T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-06-01T09:45:00,2026-06-01T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-06-01T10:35:00,2026-06-01T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-06-01T12:10:00,2026-06-01T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2026-06-01T13:00:00,2026-06-01T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2026-06-01T13:55:00,2026-06-01T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2026-06-02T08:00:00,2026-06-02T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-06-02T08:50:00,2026-06-02T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-06-02T09:45:00,2026-06-02T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-06-02T10:35:00,2026-06-02T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2026-06-02T12:10:00,2026-06-02T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-06-02T13:00:00,2026-06-02T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2026-06-02T13:55:00,2026-06-02T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2026-06-03T08:00:00,2026-06-03T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2026-06-04T08:00:00,2026-06-04T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-06-04T08:50:00,2026-06-04T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-06-04T09:45:00,2026-06-04T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-06-04T10:35:00,2026-06-04T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2026-06-04T12:10:00,2026-06-04T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2026-06-04T13:00:00,2026-06-04T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2026-06-05T08:00:00,2026-06-05T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-06-05T08:50:00,2026-06-05T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-06-05T09:45:00,2026-06-05T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2026-06-05T12:10:00,2026-06-05T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-06-05T13:00:00,2026-06-05T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2026-06-05T14:45:00,2026-06-05T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2026-06-08T08:00:00,2026-06-08T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2026-06-08T08:50:00,2026-06-08T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-06-08T09:45:00,2026-06-08T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-06-08T10:35:00,2026-06-08T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-06-08T12:10:00,2026-06-08T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2026-06-08T13:00:00,2026-06-08T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2026-06-08T13:55:00,2026-06-08T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2026-06-09T08:00:00,2026-06-09T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-06-09T08:50:00,2026-06-09T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-06-09T09:45:00,2026-06-09T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-06-09T10:35:00,2026-06-09T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2026-06-09T12:10:00,2026-06-09T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-06-09T13:00:00,2026-06-09T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2026-06-09T13:55:00,2026-06-09T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2026-06-10T08:00:00,2026-06-10T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2026-06-11T08:00:00,2026-06-11T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-06-11T08:50:00,2026-06-11T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-06-11T09:45:00,2026-06-11T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-06-11T10:35:00,2026-06-11T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2026-06-11T12:10:00,2026-06-11T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2026-06-11T13:00:00,2026-06-11T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2026-06-12T08:00:00,2026-06-12T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-06-12T08:50:00,2026-06-12T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-06-12T09:45:00,2026-06-12T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2026-06-12T12:10:00,2026-06-12T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-06-12T13:00:00,2026-06-12T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2026-06-12T14:45:00,2026-06-12T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2026-06-15T08:00:00,2026-06-15T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2026-06-15T08:50:00,2026-06-15T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-06-15T09:45:00,2026-06-15T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-06-15T10:35:00,2026-06-15T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-06-15T12:10:00,2026-06-15T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2026-06-15T13:00:00,2026-06-15T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2026-06-15T13:55:00,2026-06-15T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2026-06-16T08:00:00,2026-06-16T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-06-16T08:50:00,2026-06-16T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-06-16T09:45:00,2026-06-16T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-06-16T10:35:00,2026-06-16T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2026-06-16T12:10:00,2026-06-16T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-06-16T13:00:00,2026-06-16T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2026-06-16T13:55:00,2026-06-16T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2026-06-17T08:00:00,2026-06-17T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2026-06-18T08:00:00,2026-06-18T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-06-18T08:50:00,2026-06-18T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-06-18T09:45:00,2026-06-18T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-06-18T10:35:00,2026-06-18T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2026-06-18T12:10:00,2026-06-18T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2026-06-18T13:00:00,2026-06-18T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2026-06-19T08:00:00,2026-06-19T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-06-19T08:50:00,2026-06-19T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-06-19T09:45:00,2026-06-19T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2026-06-19T12:10:00,2026-06-19T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-06-19T13:00:00,2026-06-19T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2026-06-19T14:45:00,2026-06-19T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Samfunnskunnskap,2026-06-22T08:00:00,2026-06-22T08:45:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Samfunnskunnskap,2026-06-22T08:50:00,2026-06-22T09:35:00,Mandag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-06-22T09:45:00,2026-06-22T10:30:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-06-22T10:35:00,2026-06-22T11:20:00,Mandag,,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-06-22T12:10:00,2026-06-22T12:55:00,Mandag,H118,2ITKB/ITK2002,Undervisningsøkt
Norsk,2026-06-22T13:00:00,2026-06-22T13:45:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Norsk,2026-06-22T13:55:00,2026-06-22T14:40:00,Mandag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
Utvikling,2026-06-23T08:00:00,2026-06-23T08:45:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-06-23T08:50:00,2026-06-23T09:35:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-06-23T09:45:00,2026-06-23T10:30:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-06-23T10:35:00,2026-06-23T11:20:00,Tirsdag,H118,2ITKB/ITK2003,Undervisningsøkt
Driftsstøtte,2026-06-23T12:10:00,2026-06-23T12:55:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-06-23T13:00:00,2026-06-23T13:45:00,Tirsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Norsk,2026-06-23T13:55:00,2026-06-23T14:40:00,Tirsdag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
YFF bedrift,2026-06-24T08:00:00,2026-06-24T15:30:00,Onsdag,,2ITKA + 2ITKB,Aktivitet
Driftsstøtte,2026-06-25T08:00:00,2026-06-25T08:45:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-06-25T08:50:00,2026-06-25T09:35:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-06-25T09:45:00,2026-06-25T10:30:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Driftsstøtte,2026-06-25T10:35:00,2026-06-25T11:20:00,Torsdag,H118,2ITKB/ITK2001,Undervisningsøkt
Kroppsøving vg2,2026-06-25T12:10:00,2026-06-25T12:55:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Kroppsøving vg2,2026-06-25T13:00:00,2026-06-25T13:45:00,Torsdag,,2ITKA/2ITKB/KRO1018/1,Undervisningsøkt
Samfunnskunnskap,2026-06-26T08:00:00,2026-06-26T08:45:00,Fredag,H120,2ITKA/2ITKB/SAK1001,Undervisningsøkt
Brukerstøtte,2026-06-26T08:50:00,2026-06-26T09:35:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Brukerstøtte,2026-06-26T09:45:00,2026-06-26T10:30:00,Fredag,H118,2ITKB/ITK2002,Undervisningsøkt
Utvikling,2026-06-26T12:10:00,2026-06-26T12:55:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Utvikling,2026-06-26T13:00:00,2026-06-26T13:45:00,Fredag,H118,2ITKB/ITK2003,Undervisningsøkt
Norsk,2026-06-26T14:45:00,2026-06-26T15:30:00,Fredag,,2ITKA/2ITKB/NOR1262/1,Undervisningsøkt
"""

# Create ICS content
ics_content = csv_to_ics(csv_text)

# Save to file
with open("schedule.ics", "w", encoding="utf-8") as f:
    f.write(ics_content)

print("ICS file created: schedule.ics")
