source "https://rubygems.org"

# Use Jekyll directly instead of github-pages for better Ruby 2.6 compatibility
gem "jekyll", "~> 3.8.5"

gem "tzinfo-data"
gem "wdm", "~> 0.1.0" if Gem.win_platform?

# Force older ffi version for Ruby 2.6 compatibility
gem "ffi", "~> 1.15.0"

# Individual plugins compatible with Ruby 2.6
group :jekyll_plugins do
  gem "jekyll-paginate", "~> 1.1.0"
  gem "jekyll-sitemap", "~> 1.2.0"
  gem "jekyll-gist", "~> 1.5.0"
  gem "jekyll-feed", "~> 0.12.0"
  # gem "jemoji", "~> 0.12"  # Removed due to Ruby 2.6 compatibility issues
  gem "jekyll-include-cache", "~> 0.1.0"
end
