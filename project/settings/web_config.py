# from fast_boot.security_lite.filters.filter_security_interceptor import FilterSecurityInterceptor
# from fast_boot.security_lite.http_security import HttpSecurity
# from fast_boot.security_lite.web_security_configurer_adapter import WebSecurityConfigurerAdapter
#
# from apps.security.document.services import DocumentInterceptor
#
#
# class WebConfig(WebSecurityConfigurerAdapter):
#     def configure(self, http: HttpSecurity) -> None:
#         http.authorize_requests() \
#             .regex_matchers(None, "/login*").permit_all()\
#             # .regex_matchers(None, "/test").has_role("hihi")
#
#         http.add_filter_at_offset_of(DocumentInterceptor(), 1, FilterSecurityInterceptor)
