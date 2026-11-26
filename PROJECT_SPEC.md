# Executive Intelligence AI — Project Specification

## Goal
Create a secure, responsive shared workspace for executive operations, medical robotics CRM, analytics, files, Excel intelligence, event monitoring, and AI-assisted work.

## Principles
- One authoritative, organization-scoped source of business records.
- Desktop-focused information density with mobile-responsive layouts.
- Separate Executive and Executive Assistant accounts with role-based access to shared authorized records.
- No fabricated production metrics, records, conferences, or AI answers.
- Numerical analysis must come from authorized persisted records; show empty states when records are absent.
- AI must use constrained tools, cite sources, distinguish facts from recommendations, and seek confirmation for consequential actions.
- Preserve uploaded originals; preview mappings and conflicts; never silently overwrite records.
- Treat files and web content as untrusted input. Keep API secrets server-side.
- Do not claim a capability works until it has been implemented and tested.

## Modules
Executive Overview; Copilot-inspired AI Assistant; private File Manager; Power BI-style Analytics; Medical Robotics CRM (hospitals, professionals, products, robot assets, sales, payments, installations and service); Excel workbook inspection/import; verified events; tasks/projects; calendar/meetings; follow-ups; notifications; reports; settings, users and audit history.

## Visual direction
Use the supplied 12 screens as references: deep navy, blue/violet accents, clear typography, grouped navigation, compact data-dense panels, responsive behavior, and meaningful loading/empty/error states. Figures in the designs are illustrative only.

## Security and integrity
Every protected operation must check organization membership and authorization server-side. Use secure password hashing and session management, private file storage, audit significant changes, and require review for import conflicts. Passkeys must never store biometric templates; test registration, login, fallback, recovery, and authorization before claiming support.

## Phase 0 boundary
Documentation, initial responsive frontend shell, and API health check only. No database, authentication, real AI, file persistence, or business workflows yet. Do not use this milestone for real organizational data.
