#pragma once
#ifndef BLURPLUGIN_H
#define BLURPLUGIN_H

#include <QWindow>
#include <QRegion>
#include <QObject>
#include <QGuiApplication>
#include <QQuickWindow>
#include <QtGui/QPlatformNativeInterface>  // Se necessário, mas é possível que não seja

include_directories(${Qt6Gui_INCLUDE_DIRS})

// Função externa para habilitar o blur
extern "C" void enable_blur(QQuickWindow *window);

class BlurPlugin : public QObject {
    Q_OBJECT
public:
    // Construtor padrão
    BlurPlugin(QObject *parent = nullptr) : QObject(parent) {}

    // Função para configurar o blur, invocável do QML
    Q_INVOKABLE void setBlur(QObject* window, int radius = 100);
};

#endif // BLURPLUGIN_H
