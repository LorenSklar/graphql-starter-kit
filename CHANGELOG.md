# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Project structure for open source release
- CONTRIBUTING.md with contribution guidelines
- CHANGELOG.md for version tracking
- Examples directory with sample queries
- GitHub workflows for CI/CD

### Changed
- Updated README.md with comprehensive documentation
- Improved project structure and organization

## [1.0.0] - 2024-01-15

### Added
- **Unified GraphQL API** with multiple functionalities
  - Hello/Ping queries for health checks
  - Counter with increment/set mutations
  - Logs with filtering, pagination, and statistics
- **SQLite database** with direct SQL queries (no ORM)
- **CSV data ingestion** for log data
- **Production-ready** uvicorn ASGI server
- **Comprehensive documentation** with examples
- **Sample data generation** using fake-log-generator
- **Project rules and requirements** documentation

### Features
- **Hello/Ping**: Basic health checks and greetings
  - `hello(name: String)` - Personalized greetings
  - `ping` - Health check endpoint
- **Counter**: Stateful counter with mutations
  - `counter` - Get current value
  - `incrementCounter` - Increment by 1
  - `setCounter(value: Int!)` - Set to specific value
- **Logs**: Web request log data with advanced features
  - `logs()` - Paginated log retrieval with filtering
  - `log(id: ID!)` - Single log by ID
  - `logStats` - Statistics and analytics
  - Filtering by: log_level, service_name, status_code, env
  - Pagination with offset and limit
  - Statistics by level, service, status, and environment

### Technical Details
- **Database**: SQLite with direct SQL queries
- **GraphQL**: Ariadne framework with ASGI
- **Server**: uvicorn ASGI server
- **Data Format**: CSV with proper escaping
- **Schema**: 23-column log structure matching production logs

### Documentation
- **README.md**: Comprehensive setup and usage guide
- **rules.md**: Project requirements and schema documentation
- **GraphQL Examples**: Named queries and mutations for easy testing
- **CSV Format**: Detailed schema specification
- **Deployment**: Production-ready configuration

### Dependencies
- ariadne==0.26.2
- uvicorn==0.24.0
- pandas>=2.2.0
- python-multipart==0.0.6

---

## Version History

- **1.0.0**: Initial release with unified GraphQL API
- **Unreleased**: Open source preparation and documentation

## Migration Guide

### From Previous Versions
This is the initial release, so no migration is needed.

### Breaking Changes
None in this release.

### Deprecations
None in this release.

---

For detailed information about each release, see the [GitHub releases page](https://github.com/LorenSklar/graphql-starter-kit/releases). 