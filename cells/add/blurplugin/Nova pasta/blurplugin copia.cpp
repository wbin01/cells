#include "blurplugin.h"
#include <QQuickWindow>
#include <QVariant>
#include <QDebug>

void BlurPlugin::setBlur(QObject* window, int radius) {
    QWindow* qwindow = qobject_cast<QWindow*>(window);
    if (!qwindow) {
        qDebug() << "Objeto não é uma QWindow válida";
        return;
    }

    QRegion region(0, 0, qwindow->width(), qwindow->height());
    qwindow->setProperty("_q_platformBlurRegion", region);
    qDebug() << "Blur aplicado com região:" << region;
}
