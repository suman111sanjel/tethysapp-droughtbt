from tethys_sdk.base import TethysAppBase, url_map_maker


class Droughtbt(TethysAppBase):
    """
    Tethys app class for Droughtbt.
    """

    name = 'Drought Watch - Bhutan'
    index = 'droughtbt:Home'
    icon = 'droughtbt/images/icon.gif'
    package = 'droughtbt'
    root_url = 'droughtbt'
    color = '#2c3e50'
    description = ''
    tags = 'Drought-Watch'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='Home',
                url='droughtbt',
                controller='droughtbt.controllers.Current.home'
            ),UrlMap(
                name='CurrentHome',
                url='droughtbt/current',
                controller='droughtbt.controllers.Current.home'
            ), UrlMap(
                name='SeasonalHome',
                url='droughtbt/seasonal',
                controller='droughtbt.controllers.Seasonal.home'
            ), UrlMap(
                name='OutlookHome',
                url='droughtbt/outlook',
                controller='droughtbt.controllers.Outlook.home'
            ),
            UrlMap(
                name='geomList',
                url='api/getGeomList',
                controller='droughtbt.api.getGeomList'
            ),
            UrlMap(
                name='Stats',
                url='api/getJsonFromAPI',
                controller='droughtbt.api.getJsonFromBLDAS'
            ),
            UrlMap(
                name='AreaUnder',
                url='api/getAreaUnder',
                controller='droughtbt.api.getAreaUnderFromBLDAS'
            ),
            UrlMap(
                name='LTAstats',
                url='api/getLTAStats',
                controller='droughtbt.api.getLTAStats'
            ),
            UrlMap(
                name='SAAreaUnder',
                url='api/seasonagg',
                controller='droughtbt.api.getSeasonalAggregatedRatio'
            ),
            UrlMap(
                name='PercentageOfNormal',
                url='api/percentageOfNormal',
                controller='droughtbt.api.getPercentageOfNormal'
            ),
            UrlMap(
                name='forecast',
                url='api/getSpatialAverageForecast',
                controller='droughtbt.api.getSpatialAverageForecast'
            ),
        )

        return url_maps

