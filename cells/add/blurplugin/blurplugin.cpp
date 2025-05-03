
#include <QQuickWindow>
#include <QGuiApplication>
#include <wayland-client.h>
#include "blur-client-protocol.h"

static org_kde_kwin_blur_manager *blur_manager = nullptr;

void registry_handler(void *, wl_registry *registry, uint32_t id,
                      const char *interface, uint32_t)
{
    if (strcmp(interface, "org_kde_kwin_blur_manager") == 0) {
        blur_manager = static_cast<org_kde_kwin_blur_manager *>(
            wl_registry_bind(registry, id, &org_kde_kwin_blur_manager_interface, 1));
    }
}

void registry_remover(void *, wl_registry *, uint32_t) {}

void enable_blur(QQuickWindow *window)
{
    wl_display *display = static_cast<wl_display *>(
        QGuiApplication::platformNativeInterface()->nativeResourceForWindow("display", window));
    wl_surface *surface = static_cast<wl_surface *>(
        QGuiApplication::platformNativeInterface()->nativeResourceForWindow("surface", window));

    wl_registry *registry = wl_display_get_registry(display);

    static const wl_registry_listener listener = {
        .global = registry_handler,
        .global_remove = registry_remover
    };

    wl_registry_add_listener(registry, &listener, nullptr);
    wl_display_roundtrip(display);

    if (blur_manager && surface) {
        org_kde_kwin_blur *blur = org_kde_kwin_blur_manager_create(blur_manager, surface);
        Q_UNUSED(blur);
    }
}
