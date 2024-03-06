from django.contrib import admin


from .models import Artwork, AuctionItem

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'image', 'description')

@admin.register(AuctionItem)
class AuctionItemAdmin(admin.ModelAdmin):
    list_display = ('artwork', 'start_time', 'end_time', 'current_bid', 'current_bid_user', 'is_active')
    list_filter = ('start_time', 'end_time', 'current_bid_user')
    search_fields = ('artwork__title', 'artwork__artist')

