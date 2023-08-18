#list of phrases that job_level_decoder.py uses to classify level of job ads
#to add a phrase first add to list of phrases for correct level and then add weight to corresponding dictionary
list_low_title = [
    'eit',
    'e.i.t',
    'new grad',
    'engineer-in-training',
    'engineer in training',
    'entry level',
    'managed',
    'junior',
    'jr',
    'new college grad',
    'intern',
    'co-op',
    'student',
    'graduate',
]

list_low_ad = [
    ' 0-',
    'under the direction',
    'under the supervision',
    'under the guidance',
    'zero to',
    'zero years',
    'entry level',
    'entry-level',
    'internship',
    'co-op',
    'current students',
    'new graduate',
    'new college grad',
    ' 0 to',
    'new grad',
    'recent grad',
    ' 1+',
    ' 0 -',
    ' 1-',
    'asset',
    'desirable',
    ' 1 year',
    'one year',
]

dict_low_title = {
    'eit' : 8,
    'e.i.t' : 8,
    'new grad' : 8,
    'engineer-in-training' : 8,
    'engineer in training' : 8,
    'entry level': 8,
    'managed' : 8,
    'junior' : 3,
    'jr' : 3,
    'new college grad' : 8,
    'intern' : 8,
    'co-op' : 8,
    'student' : 8,
    'graduate' : 8,
}

dict_low_ad = {
    ' 0-' : 4,
    'under the direction' : 4,
    'under the supervision': 4,
    'under the guidance' : 4,
    'zero to' : 4,
    'zero years': 4,
    'entry level': 4,
    'entry-level' : 4,
    'internship' : 3,
    'co-op' : 3,
    'current students' : 3,
    'new graduate' : 4,
    'new college grad': 4,
    ' 0 to' : 4,
    'new grad' : 4,
    'recent grad' : 4,
    ' 1+' : 4,
    ' 0 -' : 4,
    ' 1-' : 4,
    'asset' : 2,
    'desirable' : 2,
    ' 1 year' : 3,
    'one year' : 4,
}

list_medium_title = [
    'intermediate',
]

list_medium_ad = [
    'independent',
    ' 3-',
    'more senior',
    'minimum 3',
    'proficien',
    'report to',
    'reporting to',
    'reports to',
    'intermediate',
    '3+',
    'mid-level',
    'minimal supervision',
    '5+',
    '4 years',
    '2+ years',
    ' 5-',
    ' 5 years',
    '1-5 years',
    '6+ years',
    '+5 years',
    ' 3 years',
    ' to 8 years',
    ' four years',
    'professional engineer',
    '2 years',
    ' 2-',
    ' 6 years',
    ' 4+',
    ' five years',
    ' excellence',
    ' three years',
    'asset',
    'desirable',
    ' an experienced',
    'experience in',
    'experience working in',
    'previous experience',
    'proven experience',
    '(5) years',
    '(2) years',
    '(3) years',
    '(4) years',
    ' 3 to ',
]

dict_medium_title = {
    'intermediate' : 8,
}

dict_medium_ad = {
    'independent' : 2,
    ' 3-' : 4,
    'more senior' : 4,
    'minimum 3' : 4,
    'proficien' : 1,
    'report to' : 2,
    'reporting to' : 3,
    'reports to' : 3,
    'intermediate' : 4,
    '3+' : 4,
    'mid-level' : 4,
    'minimal supervision' : 4,
    '5+' : 2,
    '4 years' : 3,
    '2+ years' : 4,
    ' 5-' : 4,
    ' 5 years' : 1,
    '1-5 years' : 4,
    '6+ years' : 1,
    '+5 years' : 2,
    ' 3 years' : 2,
    ' to 8 years' : 2,
    ' four years' : 3,
    'professional engineer' : 1,
    '2 years' : 1,
    ' 2-' : 4,
    ' 6 years' : 4,
    ' 4+' : 4,
    ' five years' : 1,
    ' excellence' : 2,
    ' three years' : 2,
    'asset' : 2,
    'desirable' : 2,
    ' an experienced' : 4,
    'experience in' : 3,
    'experience working in' : 3,
    'previous experience' : 3,
    'proven experience' : 3,
    '(5) years' : 1,
    '(2) years' : 1,
    '(3) years' : 3,
    '(4) years' : 3,
    ' 3 to ' : 4,
}

list_high_title = [
    'senior',
    'sr',
    'lead',
    'research chair',
    'manager',
]

list_high_ad = [
    'minimum 10',
    'engineering lead',
    'minimum of 7',
    'oversee',
    'minimum of 15',
    'leadership experience',
    '10 years',
    '7+',
    'ten years',
    'eight years',
    'technical direction',
    'professional engineer',
    'team lead',
    ' 10+',
    '15 years',
    ' 8 years',
    '12 years',
    '7 years',
    ' training experience',
    'establish',
    'team lead',
    ' an experienced',
    'experience in',
    'experience working in',
    'previous experience',
    'proven experience',
    '8+ years',
    'proficien',
]

dict_high_title = {
    'senior' : 8,
    'sr' : 8,
    'lead' : 8,
    'research chair' : 1,
    'manager' : 8,
}

dict_high_ad = {
    'minimum 10' : 4,
    'engineering lead' : 4,
    'minimum of 7' : 3,
    'oversee' : 2,
    'minimum of 15' : 4,
    'leadership experience' : 4,
    '10 years' : 4,
    '7+' : 3,
    'ten years' : 4,
    'eight years' : 4,
    'technical direction' : 2,
    'professional engineer' : 1,
    'team lead' : 2,
    ' 10+' : 4,
    '15 years' : 4,
    ' 8 years' : 4,
    '12 years' : 4,
    '7 years' : 4,
    ' training experience' : 4,
    'establish' : 3,
    'team lead' : 2,
    ' an experienced' : 4,
    'experience in' : 2,
    'experience working in' : 2,
    'previous experience' : 2,
    'proven experience' : 2,
    '8+ years' : 4,
    'proficien' : 2,
}
