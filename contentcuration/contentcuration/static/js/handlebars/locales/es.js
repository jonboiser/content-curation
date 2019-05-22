HandlebarsIntl.__addLocaleData({
  locale: 'es',
  pluralRuleFunction: function(n, ord) {
    if (ord) return 'other';
    return n == 1 ? 'one' : 'other';
  },
  fields: {
    year: {
      displayName: 'Año',
      relative: { '0': 'este año', '1': 'el próximo año', '-1': 'el año pasado' },
      relativeTime: {
        future: { one: 'dentro de {0} año', other: 'dentro de {0} años' },
        past: { one: 'hace {0} año', other: 'hace {0} años' },
      },
    },
    month: {
      displayName: 'Mes',
      relative: { '0': 'este mes', '1': 'el próximo mes', '-1': 'el mes pasado' },
      relativeTime: {
        future: { one: 'dentro de {0} mes', other: 'dentro de {0} meses' },
        past: { one: 'hace {0} mes', other: 'hace {0} meses' },
      },
    },
    day: {
      displayName: 'Día',
      relative: {
        '0': 'hoy',
        '1': 'mañana',
        '2': 'pasado mañana',
        '-1': 'ayer',
        '-2': 'antes de ayer',
      },
      relativeTime: {
        future: { one: 'dentro de {0} día', other: 'dentro de {0} días' },
        past: { one: 'hace {0} día', other: 'hace {0} días' },
      },
    },
    hour: {
      displayName: 'Hora',
      relativeTime: {
        future: { one: 'dentro de {0} hora', other: 'dentro de {0} horas' },
        past: { one: 'hace {0} hora', other: 'hace {0} horas' },
      },
    },
    minute: {
      displayName: 'Minuto',
      relativeTime: {
        future: { one: 'dentro de {0} minuto', other: 'dentro de {0} minutos' },
        past: { one: 'hace {0} minuto', other: 'hace {0} minutos' },
      },
    },
    second: {
      displayName: 'Segundo',
      relative: { '0': 'ahora' },
      relativeTime: {
        future: { one: 'dentro de {0} segundo', other: 'dentro de {0} segundos' },
        past: { one: 'hace {0} segundo', other: 'hace {0} segundos' },
      },
    },
  },
});
HandlebarsIntl.__addLocaleData({
  locale: 'es-419',
  parentLocale: 'es',
  fields: {
    year: {
      displayName: 'Año',
      relative: { '0': 'Este año', '1': 'Año próximo', '-1': 'Año pasado' },
      relativeTime: {
        future: { one: 'En {0} año', other: 'En {0} años' },
        past: { one: 'hace {0} año', other: 'hace {0} años' },
      },
    },
    month: {
      displayName: 'Mes',
      relative: { '0': 'Este mes', '1': 'Mes próximo', '-1': 'El mes pasado' },
      relativeTime: {
        future: { one: 'En {0} mes', other: 'En {0} meses' },
        past: { one: 'hace {0} mes', other: 'hace {0} meses' },
      },
    },
    day: {
      displayName: 'Día',
      relative: {
        '0': 'hoy',
        '1': 'mañana',
        '2': 'pasado mañana',
        '-1': 'ayer',
        '-2': 'antes de ayer',
      },
      relativeTime: {
        future: { one: 'En {0} día', other: 'En {0} días' },
        past: { one: 'hace {0} día', other: 'hace {0} días' },
      },
    },
    hour: {
      displayName: 'Hora',
      relativeTime: {
        future: { one: 'En {0} hora', other: 'En {0} horas' },
        past: { one: 'hace {0} hora', other: 'hace {0} horas' },
      },
    },
    minute: {
      displayName: 'Minuto',
      relativeTime: {
        future: { one: 'En {0} minuto', other: 'En {0} minutos' },
        past: { one: 'hace {0} minuto', other: 'hace {0} minutos' },
      },
    },
    second: {
      displayName: 'Segundo',
      relative: { '0': 'ahora' },
      relativeTime: {
        future: { one: 'En {0} segundo', other: 'En {0} segundos' },
        past: { one: 'hace {0} segundo', other: 'hace {0} segundos' },
      },
    },
  },
});
HandlebarsIntl.__addLocaleData({ locale: 'es-AR', parentLocale: 'es-419' });
HandlebarsIntl.__addLocaleData({ locale: 'es-BO', parentLocale: 'es-419' });
HandlebarsIntl.__addLocaleData({ locale: 'es-CL', parentLocale: 'es-419' });
HandlebarsIntl.__addLocaleData({ locale: 'es-CO', parentLocale: 'es-419' });
HandlebarsIntl.__addLocaleData({ locale: 'es-CR', parentLocale: 'es-419' });
HandlebarsIntl.__addLocaleData({ locale: 'es-CU', parentLocale: 'es-419' });
HandlebarsIntl.__addLocaleData({ locale: 'es-DO', parentLocale: 'es-419' });
HandlebarsIntl.__addLocaleData({ locale: 'es-EA', parentLocale: 'es' });
HandlebarsIntl.__addLocaleData({ locale: 'es-EC', parentLocale: 'es-419' });
HandlebarsIntl.__addLocaleData({ locale: 'es-ES', parentLocale: 'es' });
HandlebarsIntl.__addLocaleData({ locale: 'es-GQ', parentLocale: 'es' });
HandlebarsIntl.__addLocaleData({ locale: 'es-GT', parentLocale: 'es-419' });
HandlebarsIntl.__addLocaleData({ locale: 'es-HN', parentLocale: 'es-419' });
HandlebarsIntl.__addLocaleData({ locale: 'es-IC', parentLocale: 'es' });
HandlebarsIntl.__addLocaleData({
  locale: 'es-MX',
  parentLocale: 'es-419',
  fields: {
    year: {
      displayName: 'Año',
      relative: { '0': 'este año', '1': 'el año próximo', '-1': 'el año pasado' },
      relativeTime: {
        future: { one: 'En {0} año', other: 'En {0} años' },
        past: { one: 'hace {0} año', other: 'hace {0} años' },
      },
    },
    month: {
      displayName: 'Mes',
      relative: { '0': 'este mes', '1': 'el mes próximo', '-1': 'el mes pasado' },
      relativeTime: {
        future: { one: 'en {0} mes', other: 'en {0} meses' },
        past: { one: 'hace {0} mes', other: 'hace {0} meses' },
      },
    },
    day: {
      displayName: 'Día',
      relative: {
        '0': 'hoy',
        '1': 'mañana',
        '2': 'pasado mañana',
        '-1': 'ayer',
        '-2': 'antes de ayer',
      },
      relativeTime: {
        future: { one: 'En {0} día', other: 'En {0} días' },
        past: { one: 'hace {0} día', other: 'hace {0} días' },
      },
    },
    hour: {
      displayName: 'Hora',
      relativeTime: {
        future: { one: 'En {0} hora', other: 'En {0} horas' },
        past: { one: 'hace {0} hora', other: 'hace {0} horas' },
      },
    },
    minute: {
      displayName: 'Minuto',
      relativeTime: {
        future: { one: 'En {0} minuto', other: 'En {0} minutos' },
        past: { one: 'hace {0} minuto', other: 'hace {0} minutos' },
      },
    },
    second: {
      displayName: 'Segundo',
      relative: { '0': 'ahora' },
      relativeTime: {
        future: { one: 'En {0} segundo', other: 'En {0} segundos' },
        past: { one: 'hace {0} segundo', other: 'hace {0} segundos' },
      },
    },
  },
});
HandlebarsIntl.__addLocaleData({ locale: 'es-NI', parentLocale: 'es-419' });
HandlebarsIntl.__addLocaleData({ locale: 'es-PA', parentLocale: 'es-419' });
HandlebarsIntl.__addLocaleData({ locale: 'es-PE', parentLocale: 'es-419' });
HandlebarsIntl.__addLocaleData({ locale: 'es-PH', parentLocale: 'es' });
HandlebarsIntl.__addLocaleData({ locale: 'es-PR', parentLocale: 'es-419' });
HandlebarsIntl.__addLocaleData({ locale: 'es-PY', parentLocale: 'es-419' });
HandlebarsIntl.__addLocaleData({ locale: 'es-SV', parentLocale: 'es-419' });
HandlebarsIntl.__addLocaleData({ locale: 'es-US', parentLocale: 'es-419' });
HandlebarsIntl.__addLocaleData({ locale: 'es-UY', parentLocale: 'es-419' });
HandlebarsIntl.__addLocaleData({ locale: 'es-VE', parentLocale: 'es-419' });
